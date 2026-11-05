import unittest
from payment_discount_split.core import run
class DomainTests(unittest.TestCase):
 def test_cent_conservation(self):
  x=run({'discount_basis_points':100,'lines':[dict(id='A',cents=33),dict(id='B',cents=33),dict(id='C',cents=34)]});self.assertEqual(x['discount_cents'],1);self.assertEqual([r['discount_cents']for r in x['lines']],[0,0,1]);self.assertEqual(sum(r['payable_cents']for r in x['lines']),99)
 def test_tie_by_id(self):
  x=run({'discount_basis_points':5000,'lines':[dict(id='B',cents=1),dict(id='A',cents=1)]});self.assertEqual([r['discount_cents']for r in x['lines']],[0,1])
 def test_full(self):self.assertEqual(run({'discount_basis_points':10000,'lines':[dict(id='A',cents=7)]})['payable_cents'],0)
