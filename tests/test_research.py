"""Bounded research: exact excerpts, tamper detection, immutable evidence changes."""
from __future__ import annotations
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from src.va import core, research

class ResearchTests(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        self.addCleanup(self.t.cleanup)
        self.root = Path(self.t.name)
        with patch.object(core, 'ENGAGEMENT_ROOT', self.root):
            self.case = core.new_engagement('Test Logistics Case', 'company', 'logistics', 'quick')
        core.update_engagement(self.case, objective='Check logistics demand', approval_owner='Owner')
        self.local_file = self.root / 'report.txt'
        self.local_file.write_text('A public report suggests 12% more cargo inquiries.\nThis is not a forecast.\n',encoding='utf-8')

    def ingest(self, locator='https://example.test/report'):
        return research.import_file(self.case, self.local_file, title='Example report',locator=locator,
                                    publisher='Example publisher')

    def claim(self, sid):
        return research.add_excerpt_claim(self.case, sid, 'Cargo inquiries reportedly increased',
                                          '12% more cargo inquiries')

    def test_import_and_brief_are_reproducible(self):
        s = self.ingest()
        c = self.claim(s['source_id'])
        self.assertTrue(research.audit(self.case)['passed'])
        r1=research.brief(self.case)
        contents=Path(r1['path']).read_text()
        self.assertIn('exact excerpt',contents.lower())
        self.assertIn(s['snapshot_sha256'],contents)
        self.assertIn(c['claim_id'],contents)
        r2=research.brief(self.case)
        self.assertFalse(r2['created'])
        self.assertEqual(r2['path'],r1['path'])
        self.assertEqual(len(core.read_json(self.case/'artifacts.json')),1)

    def test_quote_absent_rejected(self):
        s=self.ingest()
        with self.assertRaisesRegex(ValueError,'Exact excerpt'):
            research.add_excerpt_claim(self.case,s['source_id'],'Unjustified market size','$100 million annual market')
        self.assertEqual(core.read_json(self.case/'claims.json'),[])

    def test_import_rejects_binary_symlinks_and_large_files(self):
        bad=self.root/'binary.txt';bad.write_bytes(b'hello\x00world')
        with self.assertRaisesRegex(ValueError,'not plain text'):
            research.import_file(self.case,bad,title='bad',locator='local:bad')
        symlink=self.root/'alias.txt';symlink.symlink_to(self.local_file)
        with self.assertRaisesRegex(ValueError,'not a symlink'):
            research.import_file(self.case,symlink,title='bad',locator='local:bad')
        huge=self.root/'huge.txt';huge.write_bytes(b'A'* (research.MAX_SOURCE_BYTES+1))
        with self.assertRaisesRegex(ValueError,'512 KiB'):
            research.import_file(self.case,huge,title='bad',locator='local:bad')

    def test_tampered_snapshot_blocks_brief(self):
        s=self.ingest()
        self.claim(s['source_id'])
        path=research._snapshot_path(self.case,s['snapshot_sha256'])
        path.write_text('Altered content!')
        a=research.audit(self.case)
        self.assertFalse(a['passed'])
        self.assertTrue(any('Corrupted' in x for x in a['errors']))
        with self.assertRaisesRegex(ValueError,'audit failed'):
            research.brief(self.case)

    def test_source_update_carries_impact_and_preserves_original(self):
        first=self.ingest()
        cl=self.claim(first['source_id'])
        dec=core.add_decision(self.case,'Should we invest?','Explore',[cl['claim_id']])
        initial=research.brief(self.case)
        prior=Path(initial['path']).read_bytes()
        self.local_file.write_text('Revised: cargo inquiries fell by 8%.\n',encoding='utf-8')
        second=self.ingest()
        self.assertNotEqual(second['source_id'],first['source_id'])
        affected=second['possible_changes'][0]['downstream_to_review']
        ids={x['id'] for x in affected}
        self.assertIn(cl['claim_id'],ids)
        self.assertIn(dec['id'],ids)
        self.assertIn(initial['artifact_id'],ids)
        self.assertEqual(Path(initial['path']).read_bytes(),prior)
        self.assertTrue(research.audit(self.case)['passed'])
        research.add_excerpt_claim(self.case,second['source_id'],'Inquiries fell','fell by 8%')
        revised=research.brief(self.case)
        self.assertNotEqual(revised['path'],initial['path'])
        self.assertTrue(Path(revised['path']).exists())

    def test_duplicate_source_import_reuses_id(self):
        a=self.ingest()
        b=self.ingest()
        self.assertFalse(b['created'])
        self.assertEqual(a['source_id'],b['source_id'])

    def test_unbacked_old_claim_cannot_be_claimed_as_excerpt(self):
        self.ingest()
        core.add_claim(self.case,'Assumption without excerpt')
        with self.assertRaisesRegex(ValueError,'At least one'):
            research.brief(self.case)

    def test_case_scoping_rejects_foreign_source(self):
        s=self.ingest()
        with patch.object(core, 'ENGAGEMENT_ROOT', self.root):
            other=core.new_engagement('Other Client','client')
        with self.assertRaisesRegex(ValueError,'Source ID not found'):
            research.add_excerpt_claim(other,s['source_id'],'x','12%')

    def test_modified_brief_fails_integrity_and_old_snapshot_is_flagged(self):
        first=self.ingest()
        self.claim(first['source_id'])
        original=research.brief(self.case)
        self.local_file.write_text('Fresh observation: inquiries fell by 8%.\n',encoding='utf-8')
        second=self.ingest()
        status=research.audit(self.case)
        self.assertTrue(status['passed'])
        self.assertEqual(status['stale_candidate_artifacts'][0]['artifact_id'],original['artifact_id'])
        Path(original['path']).write_text('Fraudulent replacement')
        status=research.audit(self.case)
        self.assertFalse(status['passed'])
        self.assertTrue(any('artifact snapshot' in e for e in status['errors']))
        with self.assertRaisesRegex(ValueError,'audit failed'):
            research.brief(self.case)

    def test_duplicate_import_refuses_corrupted_previous_snapshot(self):
        prior=self.ingest()
        research._snapshot_path(self.case,prior['snapshot_sha256']).write_text('modified snapshot')
        with self.assertRaisesRegex(ValueError,'Corrupted'):
            self.ingest()

    def test_replaced_snapshot_directory_symlink_is_rejected(self):
        prior=self.ingest()
        directory=self.case/'research'/'snapshots'
        outside=self.root/'outside'
        directory.rename(outside)
        directory.symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError,'escaped engagement'):
            research._captured_text(self.case,core.read_json(self.case/'sources.json')[0])
