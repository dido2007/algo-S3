import itertools
import math
import unittest
import balls

class Draws:
    def __init__(self, values): self.values=iter(values); self.calls=[]
    def randrange(self, stop):
        self.calls.append(stop); x=next(self.values)
        if not 0<=x<stop: raise AssertionError('invalid test draw')
        return x

class TestQ1(unittest.TestCase):
    def test_draw(self):
        d=Draws([3]); self.assertEqual(balls.throw_one(5,d),3); self.assertEqual(d.calls,[5])
class TestQ2(unittest.TestCase):
    def test_loads(self):
        d=Draws([0,2,2,1,2]); self.assertEqual(balls.simulate(5,4,d),[1,1,3,0]); self.assertEqual(d.calls,[4]*5)
        self.assertEqual(balls.simulate(0,3,Draws([])),[0,0,0])
class TestQ3(unittest.TestCase):
    def test_counts(self):
        for x,v in [([],0),([0,1,0,4],2),([1,2],0),([0,0],2)]: self.assertEqual(balls.empty_boxes(x),v)
class TestQ4(unittest.TestCase):
    def test_formula_and_exact_enumeration(self):
        for n in range(6):
            for m in range(1,5):
                sequences=list(itertools.product(range(m),repeat=n))
                exact=sum(m-len(set(seq)) for seq in sequences)/len(sequences)
                self.assertTrue(math.isclose(balls.expected_empty(n,m),exact,abs_tol=1e-12))
class TestQ5(unittest.TestCase):
    def test_average(self):
        d=Draws([0,0,0,1,1,2]); self.assertEqual(balls.estimate_empty(2,3,3,d),4/3); self.assertEqual(d.calls,[3]*6)
        self.assertEqual(balls.estimate_empty(0,4,2,Draws([])),4)
if __name__=='__main__': unittest.main(verbosity=2)
