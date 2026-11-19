"""Deterministic tests using controlled draws; no probabilistic pass/fail."""
import unittest
import reservoir as r

class Draws:
    def __init__(self, draws): self.draws=iter(draws); self.calls=[]
    def randrange(self, stop):
        self.calls.append(stop)
        x=next(self.draws)
        if not 0 <= x < stop: raise AssertionError('invalid test draw')
        return x

class TestQ1(unittest.TestCase):
    def test_uniform_draw_api(self):
        d=Draws([3]); self.assertEqual(r.choose_index(5,d),3); self.assertEqual(d.calls,[5])

class TestQ2(unittest.TestCase):
    def test_replacement(self):
        d=Draws([0,1,0]); self.assertEqual(r.sample_one(['a','b','c','d'],d),'d'); self.assertEqual(d.calls,[2,3,4])
    def test_single(self): self.assertEqual(r.sample_one([42],Draws([])),42)

class TestQ3(unittest.TestCase):
    def test_copy(self):
        a=[1,2,3]; b=r.init_reservoir(a,2); self.assertEqual(b,[1,2]); b[0]=99; self.assertEqual(a,[1,2,3]); self.assertEqual(r.init_reservoir(a,0),[])

class TestQ4(unittest.TestCase):
    def test_updates(self):
        d=Draws([1,3,0]); self.assertEqual(r.reservoir_sample(['a','b','c','d','e'],2,d),['e','c']); self.assertEqual(d.calls,[3,4,5])
    def test_edges(self):
        self.assertEqual(r.reservoir_sample([1,2],0,Draws([])),[])
        self.assertEqual(r.reservoir_sample([1,2],2,Draws([])),[1,2])
    def test_all_draw_sequences(self):
        from collections import Counter
        from itertools import product
        counts=Counter()
        for choices in product(range(3),range(4),range(5)):
            result=r.reservoir_sample(list(range(5)),2,Draws(choices))
            counts[tuple(sorted(result))]+=1
        self.assertEqual(len(counts),10)
        self.assertEqual(set(counts.values()),{6})

class TestQ5(unittest.TestCase):
    def test_mean(self):
        d=Draws([1,3,0]); self.assertEqual(r.estimate_mean([10,20,30,40,50],2,d),40)
        self.assertEqual(r.estimate_mean([2,4,6],3,Draws([])),4)

if __name__ == '__main__': unittest.main(verbosity=2)
