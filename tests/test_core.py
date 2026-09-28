import unittest
from research.core import Candidate,allocate
class Tests(unittest.TestCase):
 def setUp(self):
  self.c=[Candidate('P','P',8,4,1),Candidate('A','H',10,6,9),Candidate('B','H',9,5,1)]
 def test_risk_changes_allocation(self):
  self.assertEqual(allocate(self.c,20,{'P':1,'H':1})['ids'],['A','P'])
  self.assertEqual(allocate(self.c,20,{'P':1,'H':1},1)['ids'],['B','P'])
 def test_budget_infeasible(self):
  self.assertIsNone(allocate(self.c,16,{'P':1,'H':1}))
 def test_unique_and_finite(self):
  with self.assertRaises(ValueError): allocate(self.c+self.c,20,{'P':1})
  with self.assertRaises(ValueError): allocate(self.c,float('nan'),{'P':1})
 def test_order_invariance(self):
  self.assertEqual(allocate(self.c,20,{'P':1,'H':1}),allocate(self.c[::-1],20,{'P':1,'H':1}))

if __name__=="__main__": unittest.main()
