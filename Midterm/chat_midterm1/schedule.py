"""Weighted Interval Scheduling: complete the five functions.
Run: python3 test_schedule.py
Jobs are (start, finish, reward); intervals are half-open.
"""


def compatible(a, b):
    """Q1 (1 pt): whether two jobs do not overlap, O(1)."""
    
    return a[1] <= b[0]  or a[0] >= b[1]


def total_reward(jobs):
    """Q2 (1 pt): sum of all rewards, O(n)."""
    if not jobs : 
        return 0 
    
    resultat = 0 
    
    for job in jobs : 
        resultat+= job[2]
        
    return resultat

def check_valid_subset(jobs) : 
    
    if not jobs : 
        return True 
    
    for i in range(len(jobs)) : 
        
        for j in range(len(jobs)) : 
            if i == j : 
                continue
            if not compatible(jobs[i],jobs[j]) :
                return False
    return True

def best_reward_naive(jobs):
    """Q3 (2 pts): optimal reward by subset enumeration, O(n² 2ⁿ)."""
    if not jobs : 
        return 0 
    
    best_reward = 0 
    n = len(jobs) 
    
    for mask in range(2**n) : 
        
        subset = []
        
        for i in range(n) :
            if(mask >>i) & 1 : 
                subset.append(jobs[i])
        
        if not check_valid_subset(subset) : 
            continue
        
        reward = total_reward(subset)
        if reward > best_reward : 
            best_reward = reward
            
    return best_reward
                
    
    


def predecessors(jobs):
    """Q4 (4 pts): predecessor indices for finish-time-sorted jobs, O(n log n)."""
    if not jobs : 
        return []
    
    pred = []
    
    for i in range(len(jobs)) : 
        if i == 0 : 
            pred.append(-1)
            continue
        j = 0
        si = jobs[i][0]
        current = -1
        while j <= i : 
            
            
            middle = (j+i)//2 
            
            if jobs[middle][1] <= si : 
                current = middle
                j = middle+1
            
            else : 
                i = middle-1
        pred.append(current)
        
    return pred
            
        


from bisect import bisect_right

def best_reward(jobs):
    """Q5 (2 pts): optimal reward by dynamic programming, O(n log n)."""

    if not jobs:
        return 0

    # Trier par date de fin sans modifier jobs
    sorted_jobs = sorted(jobs, key=lambda job: job[1])
    n = len(sorted_jobs)

    # Dates de fin des jobs triés
    ends = [job[1] for job in sorted_jobs]

    # D[k] = récompense optimale avec les k premiers jobs
    D = [0] * (n + 1)

    for k in range(1, n + 1):
        start, end, reward = sorted_jobs[k - 1]

        # Nombre de jobs précédents finissant avant start
        j = bisect_right(ends, start, 0, k - 1)

        # Ne pas prendre le job actuel
        skip = D[k - 1]

        # Prendre le job actuel
        take = reward + D[j]

        D[k] = max(skip, take)

    return D[n]