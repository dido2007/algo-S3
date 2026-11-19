"""Deterministic public tests using controlled random bits."""
import itertools
import random
import unittest
import matrix_check as m

class Bits:
 def __init__(self,values):self.values=iter(values);self.calls=[]
 def randrange(self,stop):
  self.calls.append(stop); v=next(self.values)
  if stop!=2 or v not in (0,1):raise AssertionError('invalid draw')
  return v
class TestQ1(unittest.TestCase):
 def test_product(self):
  self.assertEqual(m.mat_vec([[1,2],[-1,3]],[3,4]),[11,9])
  self.assertEqual(m.mat_vec([[0]],[9]),[0])
class TestQ2(unittest.TestCase):
 def test_bits(self):
  rng=Bits([1,0,1]);self.assertEqual(m.random_vector(3,rng),[1,0,1]);self.assertEqual(rng.calls,[2]*3)
class TestQ3(unittest.TestCase):
 def test_checker(self):
  A=[[1,2],[0,1]];B=[[2,0],[1,3]];C=[[4,6],[1,3]];bad=[[5,6],[1,3]]
  for v in ([0,0],[0,1],[1,0],[1,1]):self.assertTrue(m.check_vector(A,B,C,v))
  self.assertTrue(m.check_vector(A,B,bad,[0,1]))
  self.assertFalse(m.check_vector(A,B,bad,[1,0]))
class TestQ4(unittest.TestCase):
 def test_fixed_bits(self):
  A=[[1,0],[0,1]];B=[[1,0],[0,1]];bad=[[2,0],[0,1]]
  self.assertTrue(m.check_once(A,B,bad,Bits([0,1])))
  self.assertFalse(m.check_once(A,B,bad,Bits([1,0])))
class TestQ5(unittest.TestCase):
 def test_repeat(self):
  I=[[1,0],[0,1]];bad=[[2,0],[0,1]]
  r=Bits([0,1,1,0]);self.assertFalse(m.check_repeated(I,I,bad,3,r));self.assertEqual(r.calls,[2]*4)
  self.assertTrue(m.check_repeated(I,I,I,2,Bits([0,0,1,1])))
 def test_all_small_vectors(self):
  I=[[1,0],[0,1]];bad=[[2,0],[0,1]]
  accepted=sum(m.check_once(I,I,bad,Bits(bits)) for bits in itertools.product((0,1),repeat=2))
  self.assertEqual(accepted,2)
if __name__=='__main__':unittest.main(verbosity=2)
