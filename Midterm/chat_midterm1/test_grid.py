"""Example tests; run python3 test_grid.py."""
import unittest
import grid as g

class TestQ1(unittest.TestCase):
    def test_open(self):
        self.assertFalse(g.is_open([], 0, 0))
        self.assertFalse(g.is_open([''], 0, 0))
        self.assertTrue(g.is_open(['.#'], 0, 0))
        for r, c in [(0,1),(-1,0),(0,-1),(1,0),(0,2)]:
            self.assertFalse(g.is_open(['.#'], r, c))

class TestQ2(unittest.TestCase):
    def test_neighbors(self):
        self.assertEqual(g.neighbors(['...','...','...'], (1,1)),
                         [(0,1),(2,1),(1,0),(1,2)])
        self.assertEqual(g.neighbors(['.#','..'], (0,0)), [(1,0)])
        self.assertEqual(g.neighbors(['.'], (0,0)), [])

class TestQ3(unittest.TestCase):
    def test_distances(self):
        self.assertEqual(g.distances([], (0,0)), {})
        self.assertEqual(g.distances(['#'], (0,0)), {})
        self.assertEqual(g.distances(['.#.','...'], (0,0)),
            {(0,0):0,(1,0):1,(1,1):2,(1,2):3,(0,2):4})
        self.assertEqual(g.distances(['.#.'], (0,0)), {(0,0):0})

class TestQ4(unittest.TestCase):
    def test_components(self):
        for grid, expected in [([], []), (['###'], []), (['.'], [1]),
            (['.#.','.#.'], [2,2]), (['..#..','#####','.#...'], [1,2,2,3])]:
            with self.subTest(grid=grid):
                self.assertEqual(g.component_sizes(grid), expected)

class TestQ5(unittest.TestCase):
    def test_paths(self):
        self.assertEqual(g.shortest_path([], (0,0), (0,0)), [])
        self.assertEqual(g.shortest_path(['.'], (0,0), (0,0)), [(0,0)])
        self.assertEqual(g.shortest_path(['.#.'], (0,0), (0,2)), [])
        self.assertEqual(g.shortest_path(['..','..'], (0,0), (1,1)),
                         [(0,0),(1,0),(1,1)])
        self.assertEqual(g.shortest_path(['.#.','...'], (0,0), (0,2)),
                         [(0,0),(1,0),(1,1),(1,2),(0,2)])

if __name__ == '__main__':
    unittest.main(verbosity=2)
