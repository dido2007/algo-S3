"""Sample deterministic tests for Part II. Run: python3 test_majority.py.
These do not assess the written Q5 explanation or prove probability bounds.
"""
import unittest
from unittest.mock import patch
import majority as maj

class TestQ1(unittest.TestCase):
    def test_frequency(self):
        for a,x,result in [([],1,0),([1,1,2],1,2),([0,-1,0],0,2),([2],7,0)]:
            self.assertEqual(maj.frequency(a,x),result)

class TestQ2(unittest.TestCase):
    def test_verify(self):
        for a,x,result in [([],0,None),([1,1,2,2],1,None),([0,0,1],0,0),
                           ([-1,-1,2],-1,-1),([9],9,9),([1,1,2],2,None)]:
            self.assertEqual(maj.verify(a,x),result)

class TestQ3(unittest.TestCase):
    def test_single_draw(self):
        for index,expected in [(0,5),(1,None),(2,5),(3,5),(4,None)]:
            with self.subTest(index=index):
                with patch.object(maj.random,'randrange',return_value=index) as draw:
                    self.assertEqual(maj.one_trial([5,2,5,5,2]),expected)
                    draw.assert_called_once_with(5)
    def test_empty(self):
        with patch.object(maj.random,'randrange') as draw:
            self.assertIsNone(maj.one_trial([])); draw.assert_not_called()

class TestQ4(unittest.TestCase):
    def test_early_stop(self):
        a=[5,2,5,5,2]; original=a[:]
        with patch.object(maj.random,'randrange',side_effect=[1,3]) as draw:
            self.assertEqual(maj.find_majority(a,5),5)
            self.assertEqual(draw.call_count,2)
            self.assertEqual(a,original)
    def test_zero_majority(self):
        with patch.object(maj.random,'randrange',side_effect=[0]) as draw:
            self.assertEqual(maj.find_majority([0,0,1],3),0)
            self.assertEqual(draw.call_count,1)
    def test_all_fail(self):
        with patch.object(maj.random,'randrange',side_effect=[1,4,1]) as draw:
            self.assertIsNone(maj.find_majority([5,2,5,5,2],3))
            self.assertEqual(draw.call_count,3)
    def test_empty_zero_trials_and_no_majority(self):
        with patch.object(maj.random,'randrange') as draw:
            self.assertIsNone(maj.find_majority([],3))
            self.assertIsNone(maj.find_majority([1],0))
            draw.assert_not_called()
        with patch.object(maj.random,'randrange',side_effect=[0,1]):
            self.assertIsNone(maj.find_majority([1,2],2))

if __name__=='__main__': unittest.main(verbosity=2)
