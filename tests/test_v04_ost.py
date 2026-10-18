import tempfile
import unittest
from pathlib import Path
from src.va import ost, core

class OSTTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.case=Path(self.tmp.name)/'case'
        self.case.mkdir()
        core.write_json(self.case/'engagement.json',{'id':'case','objective':'Explore product opportunity','approval_owner':'local reviewer'})
        for col in core.ledger.COLLECTIONS:
            core.write_json(self.case/(col+'.json'),[])
        (self.case/'events.jsonl').write_text('')
        ost.start(self.case,'Improve repeat use','Repeat use within 30 days','Independent retail owners')
    def tearDown(self): self.tmp.cleanup()

    def evidence(self,kind='interview'):
        s=core.add_source(self.case,'Interview 1','research:interview-1',kind)
        c=core.add_claim(self.case,'Merchant reported delayed reconciliation',[s['id']])
        return c['id']

    def approved_add(self,kind,parent,text,claims=None,measure='',threshold=''):
        p=ost.propose(self.case,kind,parent,text,claims or [],'Analyst proposes',measure,threshold)
        ost.review(self.case,p['proposal'],'accept','reviewer-local','Reviewed draft for local use')
        return p['node_id']

    def test_requires_primary_customer_evidence_for_opportunities(self):
        with self.assertRaises(ValueError): ost.propose(self.case,'opportunity','OST-ROOT','Invented need',[], 'guessed')
        fake=self.evidence('web_article')
        with self.assertRaises(ValueError): ost.propose(self.case,'opportunity','OST-ROOT','No customer study',[fake],'only desk research')
        actual=self.evidence()
        self.approved_add('opportunity','OST-ROOT','Reconciliation takes too long',[actual])
        self.assertEqual(len(ost.state(self.case)['nodes']),2)
        self.assertFalse(ost.state(self.case)['research_readiness']['initial_interview_guideline_met_by_record_count'])

    def test_requires_test_measure_and_threshold(self):
        c=self.evidence()
        o=self.approved_add('opportunity','OST-ROOT','Reconciliation pain',[c])
        s=self.approved_add('solution',o,'Weekly summary automation')
        with self.assertRaises(ValueError): ost.propose(self.case,'test',s,'Pilot',[],'no threshold')
        t=self.approved_add('test',s,'Observe pilots',measure='task completion',threshold='>= 80% in defined sample')
        self.assertEqual(ost.state(self.case)['nodes'][t]['type'],'test')

    def test_proposals_do_not_become_active_until_review(self):
        c=self.evidence()
        p=ost.propose(self.case,'opportunity','OST-ROOT','A pain',[c],'from interview')
        self.assertNotIn(p['node_id'],ost.state(self.case)['nodes'])
        ost.review(self.case,p['proposal'],'reject','reviewer-local','Not enough evidence')
        self.assertNotIn(p['node_id'],ost.state(self.case)['nodes'])
        with self.assertRaises(ValueError):ost.review(self.case,p['proposal'],'accept','reviewer','cannot second review')

    def test_revision_history_diff_and_integrity(self):
        c=self.evidence()
        nid=self.approved_add('opportunity','OST-ROOT','Initial pain',[c])
        seq=ost.state(self.case)['events_scanned']
        p=ost.change(self.case,nid,'revise','New interview changed wording','More specific pain')
        self.assertEqual(ost.state(self.case)['nodes'][nid]['text'],'Initial pain')
        ost.review(self.case,p['proposal'],'accept','reviewer-local','Accept refinement')
        self.assertEqual(ost.state(self.case)['nodes'][nid]['text'],'More specific pain')
        self.assertEqual(len(ost.diff(self.case,seq)['changed']),1)
        path=self.case/'discovery'/'ost-events.jsonl'
        path.write_text(path.read_text().replace('More specific pain','Tampered pain'))
        self.assertFalse(ost.verify(self.case)['passed'])
        with self.assertRaises(ValueError): ost.state(self.case)

    def test_no_cross_engagement_reference(self):
        with self.assertRaises(ValueError):
            ost.propose(self.case,'opportunity','OST-ROOT','Another client interview',['CLM-9999'],'no')

    def test_general_quality_check_detects_ost_tamper(self):
        p=self.case/'discovery'/'ost-events.jsonl'
        p.write_text(p.read_text().replace('Improve repeat use','Altered outcome'))
        # Does not pass as a clean review-ready engagement even if base journal is unchanged.
        r=core.quality_check(self.case)
        self.assertTrue(any('ost journal' in b for b in r['blockers']))

    def test_cycle_and_retirement_guards(self):
        c=self.evidence()
        a=self.approved_add('opportunity','OST-ROOT','Root pain',[c]); b=self.approved_add('opportunity',a,'Sub pain',[c])
        with self.assertRaises(ValueError): ost.change(self.case,a,'move','Would cycle',parent=b)
        p=ost.change(self.case,a,'retire','No longer relevant')
        with self.assertRaises(ValueError):ost.review(self.case,p['proposal'],'accept','reviewer','Cannot retire with child')
        self.assertTrue(ost.verify(self.case)['passed'])

if __name__=='__main__': unittest.main()
