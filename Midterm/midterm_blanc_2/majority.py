"""Practice midterm, Part II. Complete Q1-Q4 and the Q5 comment.
Run: python3 test_majority.py
"""
import random


def frequency(A, x):
    """Q1 (1 pt): number of occurrences of x, in a single pass."""
    if not A : 
        return 0
    count = 0 
    
    for i in range(len(A)) : 
        if A[i] == x : count += 1 
        
    return count 


def verify(A, x):
    """Q2 (2 pts): return x if it is a strict majority, else None."""
    
    if frequency(A,x) > len(A)/2 : 
        return x 
    
    return None


def one_trial(A):
    """Q3 (2 pts): draw one uniform position and verify its value."""
    if not A : 
        return None 
    
    i = random.randrange(len(A))
    
    return verify(A,A[i])


def find_majority(A, k):
    """Q4 (3 pts): at most k independent trials with early stopping."""
    
    if not A or k == 0 : 
        return None 
    
    for _ in range(k) : 
        
        i = random.randrange(len(A))
        if verify(A,A[i]) is not None : 
            return A[i]
        
    return None


# Q5 (2 pts): (a) exact failure probability, (b) bound depending on k,
# (c) sufficient k for failure probability <= 1/1000 and justification.
# Explain why the algorithm never returns an incorrect integer.
# Your answer: a) the failure to get not get one round is (1-f/n) so for k independannt repetition its 1-f/n)**k 
# b)we have that f is a majority, so f/n > 1/2 hence 1 -f/n < 1/2 so the proba < 1/2**k
# c) we want 2**k = 1000 so k is a peu pres egal a 10 hence we need 10 repetions 
