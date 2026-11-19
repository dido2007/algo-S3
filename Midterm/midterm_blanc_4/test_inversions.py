import random
import unittest
import inversions as inv

class TestQ1(unittest.TestCase):
    def test_pairs(self):
        for a,i,j,v in [([3,1],0,1,True),([1,1],0,1,False),([1,3],0,1,False),([3,1],1,0,False)]:
            self.assertEqual(inv.is_inversion(a,i,j),v)

class TestQ2(unittest.TestCase):
    def test_examples(self):
        for a,v in [([],0),([5],0),([3,1,2],2),([3,3,2],2),([4,3,2,1],6)]:
            self.assertEqual(inv.count_naive(a),v)

class TestQ3(unittest.TestCase):
    def test_merges(self):
        for a,b,merged,c in [([],[],[],0),([],[1,2],[1,2],0),([1,3,5],[2,3,4],[1,2,3,3,4,5],4),([2,2],[2,2],[2,2,2,2],0),([5,6],[1,2],[1,2,5,6],4)]:
            aa=a[:]; bb=b[:]
            self.assertEqual(inv.merge_count(a,b),(merged,c)); self.assertEqual((a,b),(aa,bb))

class TestQ4(unittest.TestCase):
    def test_oracle(self):
        r=random.Random(9)
        for n in range(30):
            for _ in range(10):
                a=[r.randrange(-4,5) for _ in range(n)]; old=a[:]
                count=sum(a[i]>a[j] for i in range(n) for j in range(i+1,n))
                self.assertEqual(inv.sort_count(a),(sorted(a),count)); self.assertEqual(a,old)

class TestQ5(unittest.TestCase):
    def test_rankings(self):
        r=random.Random(11)
        for n in range(9):
            for _ in range(10):
                a=list(range(n)); b=a[:]; r.shuffle(a); r.shuffle(b); pos={x:i for i,x in enumerate(b)}
                expected=sum(pos[a[i]]>pos[a[j]] for i in range(n) for j in range(i+1,n))
                self.assertEqual(inv.distance(a,b),expected)

if __name__=='__main__': unittest.main(verbosity=2)
