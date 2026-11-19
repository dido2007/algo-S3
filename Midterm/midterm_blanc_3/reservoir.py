"""CSE202 mock midterm — Problem 2. Run python3 test_reservoir.py."""
import random


def choose_index(n, rng=random):
    """Q1: uniformly sample an index in range(n), n >= 1."""
    
    return rng.randrange(n)


def sample_one(L, rng=random):
    """Q2: uniformly sample one position in nonempty L, in one pass."""
    candidat = L[0]
    for i in range(1,len(L)) : 
        index = rng.randrange(i+1)
        if index == 0 : 
            candidat = L[i]
    return candidat

# the probability since each tirage is independant hence, P(c = a) is always (n-1)! / n! = 1/n


def init_reservoir(L, k):
    """Q3: copy the first k entries, 0 <= k <= len(L)."""
    new = []
    for i in range(k) : 
        new.append(L[i])
        
    return new


def reservoir_sample(L, k, rng=random):
    """Q4: uniformly sample k positions without replacement in one pass."""
    if k == 0 :
        return []
    if k == len(L):
        return L.copy()
    reservoir = init_reservoir(L,k)
    for i in range(k,len(L)) : 
        j = rng.randrange(i+1)
        if j < k : 
            reservoir[j] = L[i]
            
    return reservoir
    # the time complexity is O(n) since, we do at maximum if k=1 n repetions and in the boucle, they are all O(1)
    # Induction : if k = i+1, hence the ith is already in so the proba is 1, and i+1 / i+1 = 1 


def estimate_mean(L, k, rng=random):
    reservoir = reservoir_sample(L, k, rng)
    return sum(reservoir) / k

# Q2 probability justification:
# TODO
# Q4 probability/complexity justification:
# TODO
