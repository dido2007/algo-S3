# -*- coding: utf-8 -*-
import math

# Q1

def poly_mult(P,Q): 
    result = [0] * (len(P) + len(Q) - 1)

    
    for i in range(len(P)) :     
        for j in range(len(Q)) :      
            result[i+j] += (P[i] * Q[j])
    
    return result
    
    
def cost_poly_mult(n): 
    return (2*n**2 - n - n +1)

# Q2

def poly_add(P,Q):
    
    if Q is None : 
        return P
    if P is None : 
        return Q
    
    smallest = P if len(P) < len(Q) else  Q
    other = Q if smallest == P else P
    
    for i in range(len(smallest)) : 
        other[i] += smallest[i]
        
    return other

def neg(P):
    
    not_P = []
    
    for i in range(len(P)) : 
        not_P.append(-P[i])
        
    return not_P
   
def shift(P,k):
   
    return [0] * k + P
    
  
# Q3  
  
def poly_kara_mult(F,G):
    if len(F) == 1 or len(G) == 1 : 
        return poly_mult(F,G)

    n = len(F)
    k = (n+1)//2
    
    F0,F1 = F[:k],F[k::]
    G0,G1 = G[:k],G[k::]
    
    H0 =  poly_kara_mult(F0,G0)
    H2 = poly_kara_mult(F1,G1)
    H1 = poly_kara_mult(poly_add(F0,F1),poly_add(G0,G1))
    
    H1_H0_H2 = poly_add(H1, poly_add(neg(H0),neg(H2)))
    
    return poly_add(poly_add(H0,shift(H1_H0_H2,k)),shift(H2,2*k))
    
    
    
def cost_poly_kara_mult(n):
    
    if n <= 1 : 
        return 1 
    
    return 3*cost_poly_kara_mult(((n+1)//2)) + 4*n

# Q4 
# Each sub-polynomial has at most ceil((n+1)/3) coefficients,
# so the size of each recursive subproblem is approximately n/3.
def cost_poly_tc3_mult(n):
    if n == 1:
        return 1
    if n == 2:
        return 3

    return 5 * cost_poly_tc3_mult((n + 2)//3) + 30*n

# Q5 hybrid
   
def poly_switch_mult(d,F,G):
    if len(F) <= d or len(G) <= d : 
            return poly_mult(F,G)
    
    n = len(F)
    k = (n+1)//2
    
    F0,F1 = F[:k],F[k::]
    G0,G1 = G[:k],G[k::]
    
    H0 =  poly_switch_mult(d,F0,G0)
    H2 = poly_switch_mult(d,F1,G1)
    H1 = poly_switch_mult(d,poly_add(F0,F1),poly_add(G0,G1))
    
    H1_H0_H2 = poly_add(H1, poly_add(neg(H0),neg(H2)))
        
    return poly_add(poly_add(H0,shift(H1_H0_H2,k)),shift(H2,2*k))

def cost_switch_mult(d,n):
    
    if n <= d : 
        return 2*n*n -2*n + 1
    
    else : 
        return 3*cost_switch_mult(d,(n+1)//2) + 4*n 

   
