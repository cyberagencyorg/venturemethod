import tempfile,unittest
from pathlib import Path
from src.va import change_model,ledger
from src.va.core import new_engagement,add_source,add_claim,add_decision,ROOT

class V03RevisionTests(unittest.TestCase):
    def setUp(self):
        self.name='test-change-v03'
        self.case=ROOT/'engagements'/self.name
        if self.case.exists():
            raise RuntimeError('Refusing to overwrite existing private engagement')
        self.case=new_engagement('Test Change V03','venture','synthetic','quick')
    def tearDown(self):
        import shutil
        shutil.rmtree(self.case)
    def test_proposal_does_not_mutate_decision(self):
        src=add_source(self.case,'notes','local:notes','synthetic')
        claim=add_claim(self.case,'Sales grew', [src['id']])
        decision=add_decision(self.case,'Expand?','Hold',[claim['id']])
        r=change_model.propose_claim_revision(self.case,claim['id'],'Sales fell','Second review',[src['id']])
        self.assertEqual(r['revision_status'],'proposed_unapproved')
        self.assertIn(decision['id'],[z['id'] for z in r['impact_on_predecessor']['downstream']])
        decision_after=next(d for d in __import__('json').loads((self.case/'decisions.json').read_text()) if d['id']==decision['id'])
        self.assertEqual(decision_after['claim_ids'],[claim['id']])
        self.assertTrue(ledger.verify(self.case)['passed'])
        with self.assertRaises(ValueError):
            change_model.propose_claim_revision(self.case,claim['id'],'Another conclusion','repeat',[src['id']])
    def test_references_scoped_to_engagement(self):
        src=add_source(self.case,'notes','local:notes','synthetic')
        claim=add_claim(self.case,'Maybe',[src['id']])
        with self.assertRaises(ValueError):
            change_model.propose_claim_revision(self.case,claim['id'],'New','why',['SRC-9999'])
    def test_impact_unknown_rejected(self):
        with self.assertRaises(ValueError): change_model.impacted(self.case,'CLM-9999')
if __name__=='__main__': unittest.main()
