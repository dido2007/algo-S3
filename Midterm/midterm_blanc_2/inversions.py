"""Practice midterm, Part I. Complete Q1-Q4 and the Q5 comment.
Run: python3 test_inversions.py
"""


def count_after(A, i):
    """Q1 (1 pt): number of j > i with A[i] > A[j]."""
    if i == len(A)-1:
        return 0
    count = 0 
    
    for j in range(i+1,len(A)) : 
        if A[i] > A[j] : count += 1 
        
    return count


def count_naive(A):
    """Q2 (2 pts): inversion count by examining pairs."""
    if not A : return 0 
    
    count = 0 
    
    for i in range(len(A)) : 
        count += count_after(A,i)
        
    return count


def merge_count(L, R):
    """Q3 (3 pts): merge sorted lists and count crossing inversions."""
    merged = []
    inversions = 0 
    
    i,j = 0,0
    
    while i < len(L) and j < len(R) : 
        if L[i] <= R[j] : 
            merged.append(L[i])
            i+=1 
        else : 
            merged.append(R[j])
            j+=1
            inversions += abs(len(L) - i)
            
    if i == len(L) : 
        merged += R[j:]
    
    if j == len(R) : 
        merged += L[i:]
        
    return (merged,inversions)


def sort_and_count(A):
    """Q4 (3 pts): return (sorted copy, inversion count) by divide-and-conquer."""
    if not A : 
        return ([],0)
    if len(A) == 1 : 
        return (A.copy(),0)
    
    
    m = len(A)//2
    count = 0
    
    L,cl = sort_and_count(A[:m])
    R,cr = sort_and_count(A[m::])

    
    merged,count_cross = merge_count(L,R)

    
    return (merged,cl+cr+count_cross)
    
# ERRORRRRRR 
def sort_and_count(A):
    """Q4 (3 pts): return (sorted copy, inversion count) by divide-and-conquer."""
    if not A : 
        return ([],0)
    if len(A) == 1 : 
        return (A.copy(),0)
    
    
    m = len(A)//2
    count = 0
    
    L = A[:m]
    R = A[m::]
    
    if len(L) == 2 and count_naive(L)== 1 :
        L = [L[1],L[0]]
        count += 1
    
    if len(R)==2 and count_naive(R)==1 : 
        R = [R[1],R[0]]
        count += 1
    
    merged,c = merge_count(sort_and_count(L),sort_and_count(R))
    count += c
    
    return (merged,count) 

# Q5 (1 pt): justify the asymptotic bound for T(n) = 2T(n/2) + Theta(n).
# Your answer:
# by master theorem a = 2 , b = 2 , c = 1 and we can see that it correspond to our algoritm since there is 2 recursive calls, <e everitiem defide our data by 2, ad the auxiliaire algoritmh is O(n)
