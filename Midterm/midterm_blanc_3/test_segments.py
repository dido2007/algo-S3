"""Public tests; success does not prove correctness or required complexity."""
import random
import unittest
import segments as s

class TestQ1(unittest.TestCase):
    def test_intervals(self):
        a = [3, -5, 2, 4]
        for i in range(len(a)+1):
            for j in range(i, len(a)+1):
                self.assertEqual(s.interval_sum(a, i, j), sum(a[i:j]))

class TestQ2(unittest.TestCase):
    def test_examples(self):
        for a, answer in [([4],4), ([-4,-1,-3],-1), ([2,-3,4,-1,2,-5],5), ([0,0],0)]:
            self.assertEqual(s.best_naive(a), answer)

class TestQ3(unittest.TestCase):
    def test_crossing(self):
        for a, lo, m, hi, answer in [([2,-3,4,-1,2,-5],0,3,6,5), ([-3,-2,-5,-1],0,2,4,-7), ([9,1,-1,3,9],1,2,4,3)]:
            self.assertEqual(s.best_crossing(a, lo, m, hi), answer)

class TestQ4(unittest.TestCase):
    def test_against_independent_oracle(self):
        rng = random.Random(88)
        for n in range(1, 30):
            for _ in range(12):
                a = [rng.randrange(-9, 10) for _ in range(n)]
                expected = max(sum(a[i:j]) for i in range(n) for j in range(i+1,n+1))
                self.assertEqual(s.best_dac(a), expected, a)

class TestQ5(unittest.TestCase):
    def test_summary(self):
        for a in [[-5], [-2,-1,-4], [2,-3,4,-1,2,-5], [0,0,0]]:
            n=len(a)
            expected=(sum(a),max(sum(a[:j]) for j in range(1,n+1)),max(sum(a[i:]) for i in range(n)),max(sum(a[i:j]) for i in range(n) for j in range(i+1,n+1)))
            self.assertEqual(s.summary(a), expected)

if __name__ == '__main__': unittest.main(verbosity=2)
