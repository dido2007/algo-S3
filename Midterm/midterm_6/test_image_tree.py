"""Public tests. Passing them does not establish correctness or complexity."""
import random
import unittest
import image_tree as q

EXAMPLE=[[0,0,1,1],[0,0,1,1],[1,0,1,1],[0,0,1,1]]
TREE=(0,1,(1,0,0,0),1)

class TestQ1(unittest.TestCase):
 def test_blocks(self):
  self.assertEqual(q.uniform_block(EXAMPLE,0,0,2),0)
  self.assertEqual(q.uniform_block(EXAMPLE,0,2,2),1)
  self.assertIsNone(q.uniform_block(EXAMPLE,2,0,2))
  self.assertEqual(q.uniform_block(EXAMPLE,2,0,1),1)
class TestQ2(unittest.TestCase):
 def test_encoding(self):
  self.assertEqual(q.encode(EXAMPLE),TREE)
  self.assertEqual(q.encode([[1]*4 for _ in range(4)]),1)
  self.assertEqual(q.encode([[0]]),0)
  a=[row[:] for row in EXAMPLE]; q.encode(a); self.assertEqual(a,EXAMPLE)
class TestQ3(unittest.TestCase):
 def test_lookup(self):
  for i in range(4):
   for j in range(4):self.assertEqual(q.pixel(TREE,4,i,j),EXAMPLE[i][j])
  self.assertEqual(q.pixel(1,8,7,0),1)
class TestQ4(unittest.TestCase):
 def test_counts(self):
  self.assertEqual(q.black_pixels(TREE,4),9)
  self.assertEqual(q.black_pixels(1,8),64)
  self.assertEqual(q.black_pixels(0,1),0)
class TestQ5(unittest.TestCase):
 def test_roundtrip(self):
  self.assertEqual(q.decode(TREE,4),EXAMPLE)
  x=q.decode(0,4); x[0][0]=1; self.assertEqual(x[1][0],0)
  rng=random.Random(24)
  for n in (1,2,4,8):
   for _ in range(8):
    image=[[rng.randrange(2) for _ in range(n)] for _ in range(n)]
    self.assertEqual(q.decode(q.encode(image),n),image)
if __name__=='__main__':unittest.main(verbosity=2)
