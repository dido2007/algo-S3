# -*- coding: utf-8 -*-
import math

### Question 1 ###
def peak_naive(L):
    # TO IMPLEMENT
    
    if len(L) == 1 :
        return 0 
    if len(L) == 2 :
        if L[0] >= L[1]: 
            return 0
        else : 
            return 1 
        
    if L[0] >= L[1] : 
        return 0 
    
    for i in range(1,len(L)-1) : 
        
        if L[i] >= L[i-1] and L[i] >= L[i+1] : 
            return i 
        
        
    if L[-1] >= L[-2] : 
        return len(L)-1
    

    
### Question 2 ###   
def peak(L):    
    # TO IMPLEMENT
    
    p,q = 0,len(L)-1
    
    return peak_aux(L,p,q)
    
def peak_aux(L,p,q):    
    # TO IMPLEMENT
    if q-p < 2 :
        if L[p]>= L[q] : 
            return p 
        else : 
            return q 
    
    l = math.floor((p+q)//2)
    
    if L[l-1] >= L[l] : 
        if L[l-1] < L[l-2] : 
            return peak_aux(L,p,l)
        else : 
            return l-1
        
    if L[l] > L[l-1] : 
        
        if L[l] < L[l+1] : 
            return peak_aux(L,l,q)     
        else : 
            return l 
    
### Question 3 ###
def is_peak(M,i,j):
    # TO IMPLEMENT
    neighbours = matrix_helper_neighbours(M,i,j) 
    
    for l,c in neighbours : 
        if M[i][j] < M[l][c] : 
            return False
    return True

def matrix_helper_neighbours(M,i,j) :  
    
    ligne = len(M)
    colonne = len(M[0])
    
    neighbours  = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    valid = []
    
    for l,c in neighbours : 
        if l < 0 or l >= ligne : 
            continue
        if c < 0 or c >= colonne : 
            continue  
        valid.append((l,c))
    return valid
### Question 4 ###
def peak2d_naive(M):
    # TO IMPLEMENT
    ligne = len(M)
    colonne = len(M[0])
    
    for i in range(ligne) : 
        
        for j in range(colonne) :
            
            if is_peak(M,i,j) : 
                return (i,j)

### Question 5 ###
def pivot(M,p,q,r,s):    
    # TO IMPLEMENT
    
    Ap = A(p,q)
    Ar = A(r,s)
    
    valid = set()
    for i in range(0,len(M)) : 
        
        for j in range(0,len(M[0])) : 
            
            if i in Ap and j >= r and j < s : 
                valid.add((i,j))
            
            if i >= p and i < q and j in Ar : 
                valid.add((i,j))
                
    maximum = - math.inf
    index = None
    
    for i,j in valid : 
        if M[i][j] > maximum : 
            maximum = M[i][j]
            index = (i,j)
            
    return index
        
            
     

def A(c,d) :
    if c >= d :
        return None  
    if d - c == 1 : 
        return [c]
    
    if d-c >= 2 : 
        l = math.floor((c+d)/2)
        return [c,l-1,l,d-1]
        
    
### Question 6 ###
def peak2d(M):    
    # TO IMPLEMENT
    p,q = 0 ,len(M)
    
    r,s = 0,len(M[0])
    
    return peak2d_aux(M,p,q,r,s) 

  
def peak2d(M):
    return peak2d_aux(M, 0, len(M), 0, len(M[0]))


def peak2d_aux(M, p, q, r, s):
    i, j = pivot(M, p, q, r, s)

    # Base case: the frame covers the entire submatrix
    if q - p <= 4 or s - r <= 4:
        return (i, j)

    if is_peak(M, i, j):
        return (i, j)

    l = (p + q) // 2
    m = (r + s) // 2

    if i < l:
        if j < m:
            return peak2d_aux(M, p, l, r, m)  
        else:
            return peak2d_aux(M, p, l, m, s)  
    else:
        if j < m:
            return peak2d_aux(M, l, q, r, m)  
        else:
            return peak2d_aux(M, l, q, m, s)  