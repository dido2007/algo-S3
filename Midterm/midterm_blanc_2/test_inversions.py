"""Sample tests for Part I. Run: python3 test_inversions.py.
These do not assess the written Q5 explanation or prove complexity bounds.
"""
import copy
import itertools
import unittest
import inversions as inv

class TestQ1(unittest.TestCase):
    def test_count_after(self):
        for a, i, expected in [([4,1,3,1],0,3),([4,1,3,1],2,1),
                               ([2,2,2],0,0),([-1,0,-2],1,1),([3],0,0)]:
            with self.subTest(a=a,i=i):
                self.assertEqual(inv.count_after(a,i),expected)

class TestQ2(unittest.TestCase):
    def test_naive(self):
        for a,expected in [([],0),([1],0),([4,1,3,1],4),([2,2,2],0),
                           ([3,2,1],3),([-1,-3,-2],2)]:
            with self.subTest(a=a):
                original=a[:]
                self.assertEqual(inv.count_naive(a),expected)
                self.assertEqual(a,original)

class TestQ3(unittest.TestCase):
    def test_merge(self):
        cases=[([],[],([],0)),([1,3,4],[1,2,5],([1,1,2,3,4,5],4)),
               ([2,2],[2,2],([2,2,2,2],0)),([5,6],[1,2],([1,2,5,6],4)),
               ([],[1,2],([1,2],0))]
        for left,right,expected in cases:
            with self.subTest(left=left,right=right):
                before=copy.deepcopy((left,right))
                self.assertEqual(inv.merge_count(left,right),expected)
                self.assertEqual((left,right),before)

class TestQ4(unittest.TestCase):
    def test_recursive(self):
        cases=[([],([],0)),([5],([5],0)),([4,1,3,1],([1,1,3,4],4)),
               ([2,2,2],([2,2,2],0)),([3,2,1],([1,2,3],3))]
        for a,expected in cases:
            with self.subTest(a=a):
                before=a[:]
                self.assertEqual(inv.sort_and_count(a),expected)
                self.assertEqual(a,before)
    def test_short_arrays(self):
        for length in range(6):
            for values in itertools.product([-1,0,1],repeat=length):
                a=list(values)
                expected=sum(a[i]>a[j] for i in range(length) for j in range(i+1,length))
                self.assertEqual(inv.sort_and_count(a),(sorted(a),expected),a)

if __name__=='__main__': unittest.main(verbosity=2)
