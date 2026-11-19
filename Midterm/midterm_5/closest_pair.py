# -*- coding: utf-8 -*-
"""CSE202 - Practice midterm, Problem 2. Closest pair of points.
Complete the five functions below.

A point is a pair (x, y) of integers. We assume all points we are given
have pairwise DISTINCT x-coordinates, and that the closest pair of a
given list of points is unique.

Run tests with: python3 test_closest_pair.py
"""


def dist2(p, q):
    """Q1 (1 pt): returns the squared Euclidean distance between the
    points p and q. O(1)."""
    # TODO
    pass


def closest_pair_naive(points):
    """Q2 (2 pts): returns a pair (best_pair, best2) where best2 is the
    minimal squared distance between two (distinct) points of the list
    `points`, and best_pair = (p, q) is a pair of points achieving it.
    Must run in O(n**2) where n = len(points), and use dist2."""
    # TODO
    pass


def closest_pair_strip(strip_sorted_by_y, best_pair, best2):
    """Q3 (2 pts): `strip_sorted_by_y` is a list of points, sorted by
    increasing y-coordinate, all lying within horizontal distance
    sqrt(best2) of some fixed vertical line (this invariant is
    guaranteed by the caller). `best_pair`/`best2` describe the best
    pair found so far elsewhere (outside the strip). The function
    returns (new_best_pair, new_best2): the best pair/squared-distance
    among best_pair and every pair of points that both lie in the
    strip. Must run in O(m) where m = len(strip_sorted_by_y).

    (Justify, in a comment below.) Explain why, to find a pair of
    points of the strip closer than the current best2, it suffices to
    compare each point of the strip to a constant number of points
    that immediately follow it in the y-sorted order (you do not need
    to find the optimal constant; any fixed bound is enough for the
    argument). Conclude that the overall running time is indeed O(m)
    and not O(m**2).
    """
    # Justify here:
    #
    # TODO
    pass


def closest_pair_rec(px, py):
    """Q4 (3 pts): px and py both list the same set of points, sorted
    by increasing x-coordinate and by increasing y-coordinate
    respectively. Returns (best_pair, best2) for this set of points,
    following the divide-and-conquer scheme:
      - if there are at most 3 points, use closest_pair_naive;
      - otherwise, split px into a left half pxl and a right half pxr
        of (near-)equal size, split py accordingly into pyl and pyr
        (keeping the sort by y-coordinate), recurse on each half,
        keep the better of the two results as (best_pair, best2), then
        build the strip of points of py within horizontal distance
        sqrt(best2) of the splitting vertical line, and call
        closest_pair_strip to possibly improve (best_pair, best2).
    """
    # TODO
    pass


def closest_pair(points):
    """Q5 (2 pts): returns a pair of points of `points` (as a 2-tuple)
    achieving the minimal distance, by sorting `points` by x and by y
    and calling closest_pair_rec. Overall complexity: O(n log n) where
    n = len(points)."""
    # TODO
    pass
