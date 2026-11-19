# -*- coding: utf-8 -*-
"""CSE202 - Practice midterm. Randomized selection (order statistics).
Complete the five functions below.

L is always a list of pairwise DISTINCT numbers.
For 1 <= k <= len(L), the k-th order statistic of L is the value that
would sit at index k-1 if L were sorted in increasing order.
Run tests with: python3 test_select.py
"""

import random


def partition_at(L, p, r, pivot_index):
    """Q1 (1 pt): in-place partition of L[p:r+1] around the pivot value
    v = L[pivot_index] (using the Lomuto scheme: swap the pivot to
    position r first, then scan). After the call, L[p:r+1] must hold
    the same elements as before, reordered so that every entry strictly
    before the returned index is <= v, the entry at the returned index
    is v, and every entry after it is > v. Must run in O(r - p + 1).
    Returns the final index of v.
    """
    # TODO
    
    v = L[pivot_index]
    
    L[pivot_index],L[r] = L[r],L[pivot_index]
    
    i = p-1
    
    for j in range(p,r) : 
        
        if L[j] <= v : 
            i+=1
            L[i],L[j] = L[j],L[i]
    
    L[i+1],L[r] = L[r],L[i+1]
    
    return i+1 
    
    


def select_sort_naive(L, k):
    """Q2 (1 pt): returns the k-th order statistic of L by sorting a
    copy of L. O(n log n) where n = len(L)."""
    # TODO
    
    return sorted(L)[k-1]


def select_fixed_pivot(L, p, r, k):
    """Q3 (2 pts): returns the k-th order statistic of the sub-list
    L[p:r+1] (1 <= k <= r - p + 1), using partition_at with
    pivot_index = r (always pivot on the last element of the current
    range), then recursing into the side that contains the answer.

    (Justify, in a comment below) Give a family of inputs L and a
    value k for which the number of recursive calls made by
    select_fixed_pivot is Theta(n); conclude that the worst-case
    complexity of this function is Theta(n**2).
    """
    # Justify here:
    # If i take a list, where a each tilme, we give as the pivor the smallest index, so we discard only 1, so we are going to do n time theta(n) = theta(n^2)
    # for example if we take an orderer list and start with the pivot as the biggest one (j'ai dit au hasard un peu)
    # TODO
    q = partition_at(L,p,r,r)
    m = q-p+1
    
    
    if k == m : 
        return L[q]
    
    elif k < m : 
        return select_fixed_pivot(L,p,q-1,k)
    
    elif k > m :
        return select_fixed_pivot(L,q+1,r,k-m)


def randomized_select(L, k):
    """Q4 (4 pts): returns the k-th order statistic of L, using the
    same divide-and-conquer scheme as select_fixed_pivot, EXCEPT that
    at each recursive call the pivot index is drawn uniformly at
    random among the indices of the current range (use
    random.randint(p, r)) instead of always being r.

    You may write an auxiliary function if you want.

    (Justify, in a comment below, 1 pt) Call a pivot choice "balanced"
    if, among the n = r - p + 1 elements of the current range, the
    pivot's rank m satisfies ceil(n/4) <= m <= ceil(3n/4). Show that a
    pivot index drawn uniformly at random among the n positions of the
    range is balanced with probability at least 1/2.

    (Justify, in a comment below, 1 pt) Using the previous question,
    argue informally why the expected number of comparisons performed
    by randomized_select is O(n).
    """
    # Justify (balanced pivot probability) here:
    # its easy to see, that, since ceil(n/4) <= m <= ceil(3n/4), so m have ceil(n/2) possible values, since its a uniform law, the propba is of 1/2
    # Justify (expected complexity) here:
    #We cann the sitation as, each 2 draws, we schrink our range by a least 3/4 
    # and so using the master thoerme with b =4/3 and f(n) = O(n) we can see that it is O(n)
    # TODO
    p,r = 0,len(L)-1
    pivot = random.randint(p,r)
    
    q = partition_at(L,p,r,pivot)
    m = q-p+1
    
    
    if k == m : 
        return L[q]
    
    elif k < m : 
        return select_fixed_pivot(L,p,q-1,k)
    
    elif k > m :
        return select_fixed_pivot(L,q+1,r,k-m)


def k_smallest_set(L, k):
    """Q5 (2 pts): returns, as a list in ANY order, the k smallest
    elements of L (1 <= k <= len(L)), with expected complexity O(n)
    where n = len(L). Hint: use randomized_select once to find the
    value of the k-th order statistic, then make a single linear pass
    over L.
    """
    # TODO
    
    v = randomized_select(L,k)
    
    result = [v]
    
    for i in range(len(L)) : 
        
        if len(result) != k : 
            
            if L[i] < v : 
                result.append(L[i])
                
    return result
    
    
