"""CSE202 mock midterm — Problem 1. Run python3 test_segments.py."""
import math

def interval_sum(A, i, j):
    """Q1: sum of A[i:j], 0 <= i <= j <= len(A). O(j-i)."""
    
    if i == j : 
        return 0
    return sum(A[i:j])


def best_naive(A):
    """Q2: maximum sum of a nonempty contiguous subarray. O(n^2)."""
    
    maximum = - math.inf
    
    
    for i in range(len(A)) : 
        somme = 0
        for j in range(i,len(A)) : 
            somme = somme + A[j]
            if somme > maximum : 
                maximum = somme
    return maximum
                
                


def best_crossing(A, lo, mid, hi):
    """Q3: best nonempty subarray crossing mid in A[lo:hi]. O(hi-lo)."""
    
    left_optimal_sum = - math.inf
    left_sum = 0 
    
    for i in range(mid-1,lo-1,-1) : 
        left_sum += A[i]
        if left_sum > left_optimal_sum : 
            left_optimal_sum = left_sum
        
    
    right_optimal_sum = - math.inf
    right_sum = 0 
    for i in range(mid,hi) : 
        right_sum += A[i]
        if right_sum > right_optimal_sum : 
            right_optimal_sum = right_sum
            
    return left_optimal_sum + right_optimal_sum


def best_dac(A):
    """Q4: maximum nonempty subarray sum using divide and conquer. O(n log n)."""
    
    if len(A) == 1 : 
        return A[0]
    
    mid = len(A)//2
    
    right_part = best_dac(A[:mid])
    left_part = best_dac(A[mid:])
    crossing = best_crossing(A,0,mid,len(A))
    
    return max(left_part,right_part,crossing)
    
    # T(n) = 2T(n/2) + O(n), à l'arrondi près.
    # Donc T(n) = O(n log n).

def summary(A):
    """Q5: return (total, best prefix, best suffix, best subarray). O(n)."""
    t = p= s= b = A[0]
    
    for i in range(1,len(A)) : 
        x = A[i]
        t,p,s,b = t+x , max(p,t+x), max(x,x+s),max(b,x,s+x)
        
    return t,p,s,b
        

# Q4 complexity justification:
# TODO
# Q5 correctness/complexity justification:
# TODO
