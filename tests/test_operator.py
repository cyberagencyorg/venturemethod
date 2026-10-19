"""First operator use: local onboarding, source-grounded handoff and unapproved return."""
from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.va import core, operator, research, composition
from va import main


class OperatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        with patch.object(core, 'ENGAGEMENT_ROOT',self.root):
            self.started=operator.start('Sample Studio Project','venture',
                          'Should we test a limited launch?',industry='transport',owner='Principal')
        self.case=self.root/self.started['engagement']
        self.sourcefile=self.root/'market.txt'
        self.sourcefile.write_text('Survey respondents reported long procurement lead times.\n'
                                   'These are self-reported experiences.\n', encoding='utf-8')

    def evidence(self):
        src=research.import_file(self.case,self.sourcefile,title='Procurement report',
                  locator='https://example.test/procurement',publisher='Unknown source')
        claim=research.add_excerpt_claim(self.case,src['source_id'],
                  'The report includes respondent accounts of slow procurement',
                  'Survey respondents reported long procurement lead times.')
        return src,claim

    def test_doctor_and_start(self):
        self.assertTrue(operator.doctor()['ready_for_local_work'])
        status=operator.status(self.case)
        self.assertTrue(status['integrity']['journal'])
        self.assertEqual(status['counts']['captured_sources'],0)
        self.assertIn('research fetch',status['next_actions'][0])
        self.assertIn('Should we test',status['objective'])

    def test_start_rejects_empty_before_creating(self):
        with self.assertRaises(ValueError): operator.start('No Objective','venture',' ')
        self.assertFalse((self.root/'no-objective').exists())

    def test_packet_before_evidence_labels_unknown(self):
        pack=operator.packet(self.case,save=False)
        self.assertIn('No source-quoted claims available',pack['markdown'])
        self.assertIn('Do not present',pack['markdown'])
        self.assertFalse((self.case/'deliverables'/('work-packet-'+pack['sha256'][:16]+'.md')).exists())

    def test_work_packet_submission_and_idempotency(self):
        src,claim=self.evidence()
        packet=operator.packet(self.case)
        self.assertTrue(packet['created'])
        text=Path(packet['path']).read_text()
        self.assertIn(src['source_id'],text)
        self.assertIn(claim['claim_id'],text)
        self.assertIn('UNTRUSTED QUOTATION',text)
        self.assertFalse(operator.packet(self.case)['created'])
        report=self.root/'submitted.md'
        report.write_text('# Proposed limited pilot\n\nThis is a provisional interpretation of '
              +src['source_id']+' and '+claim['claim_id']+'. Additional evidence needed.\n')
        s=operator.submit(self.case,report,author='External agent (operator assertion)')
        self.assertTrue(s['created'])
        self.assertEqual(s['status'],'unreviewed')
        self.assertFalse(operator.submit(self.case,report)['created'])
        self.assertEqual(operator.status(self.case)['counts']['submitted_drafts'],1)
        self.assertTrue(operator.check_submitted(self.case)['passed'])
        art=next(a for a in core.read_json(self.case/'artifacts.json') if a['kind']=='submitted-draft')
        self.assertFalse(art['publication_authorized'])
        self.assertTrue(art['needs_factual_review'])
        self.assertTrue(research.audit(self.case)['passed'])

    def test_foreign_engagement_ids_rejected(self):
        self.evidence()
        report=self.root/'bad.md'
        report.write_text('Fake SRC-9999 and CLM-9999\n')
        with self.assertRaisesRegex(ValueError,'missing from this engagement'):
            operator.submit(self.case,report)
        self.assertFalse(list((self.case/'deliverables').glob('submitted-*')))

    def test_binary_symlink_and_overlong_rejected(self):
        bad=self.root/'bad.md';bad.write_bytes(b'bad\x00text')
        with self.assertRaisesRegex(ValueError,'UTF-8'):operator.submit(self.case,bad)
        alias=self.root/'alias.md';alias.symlink_to(bad)
        with self.assertRaisesRegex(ValueError,'regular'):operator.submit(self.case,alias)
        huge=self.root/'huge.md';huge.write_bytes(b'a'*(operator.MAX_DRAFT_BYTES+1))
        with self.assertRaisesRegex(ValueError,'256 KiB'):operator.submit(self.case,huge)

    def test_tamper_detection_and_source_change(self):
        src,_=self.evidence()
        packet=operator.packet(self.case)
        report=self.root/'report.md';report.write_text('Observation from '+src['source_id'])
        submitted=operator.submit(self.case,report)
        self.sourcefile.write_text('Subsequent survey respondents reported shorter procurement times.\n')
        new=research.import_file(self.case,self.sourcefile,title='Procurement report',
                 locator='https://example.test/procurement',publisher='Unknown source')
        self.assertNotEqual(src['source_id'],new['source_id'])
        stale={x['artifact_id'] for x in operator.check_submitted(self.case)['stale_candidates']}
        self.assertIn(packet['artifact_id'],stale)
        self.assertIn(submitted['artifact_id'],stale)
        Path(submitted['path']).write_text('tampered')
        result=operator.check_submitted(self.case)
        self.assertFalse(result['passed'])
        self.assertIn('hash mismatch',result['errors'][0])


    def test_selected_plan_included_and_rejected_when_stale(self):
        self.evidence()
        plan=composition.compose(self.case,goals=['design_business'],
             method_ids=['business-model-canvas'],evidence='observed',save=True)
        name=Path(plan['saved_to']).name
        pack=operator.packet(self.case,save=False,plan_name=name)
        self.assertIn('business-model-canvas',pack['markdown'])
        self.assertIn('operator-selected proposal',pack['markdown'])
        self.assertEqual(pack['composition_plan'],name)
        self.sourcefile.write_text('New incompatible evidence.\n')
        research.import_file(self.case,self.sourcefile,title='Procurement report',
                   locator='https://example.test/procurement',publisher='Unknown source')
        with self.assertRaisesRegex(ValueError,'stale'):
            operator.packet(self.case,plan_name=name)

    def test_rejects_traversal_and_modified_plan(self):
        self.evidence()
        plan=composition.compose(self.case,goals=['design_business'],
             method_ids=['business-model-canvas'],evidence='observed',save=True)
        name=Path(plan['saved_to']).name
        with self.assertRaisesRegex(ValueError,'filename'):
            operator.packet(self.case,plan_name='../'+name)
        (self.case/plan['saved_to']).write_text('{}')
        with self.assertRaisesRegex(ValueError,'digest mismatch'):
            operator.packet(self.case,plan_name=name)

    def test_cli_end_to_end_without_network_or_model(self):
        with patch.object(core,'ENGAGEMENT_ROOT',self.root):
            out=io.StringIO()
            with contextlib.redirect_stdout(out):
                result=main(['start','Work Example','--type','client','--objective','Review a service proposal'])
            self.assertEqual(result,0)
            slug=json.loads(out.getvalue())['engagement']
            with contextlib.redirect_stdout(io.StringIO()) as captured:
                r=main(['packet',slug,'--preview'])
            self.assertEqual(r,0)
            payload=json.loads(captured.getvalue())
            self.assertIn('Review a service proposal',payload['markdown'])
            with contextlib.redirect_stdout(io.StringIO()) as captured:
                r=main(['status',slug])
            self.assertEqual(r,0)
            self.assertIn('next_actions',json.loads(captured.getvalue()))


if __name__ == '__main__':unittest.main()
