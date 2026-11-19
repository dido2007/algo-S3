# -*- coding: utf-8 -*-

import math
try:
    from PowerTree import *
except:
    pass

## Q1 ##

# binary powering, returns x^n
def bin_pow(x, n):
    if n == 0 : 
        return 1 
    if n == 1 : 
        return x 
    
    exp = bin_pow(x,math.floor(n/2))
    if n % 2 == 0 : 
        return exp**2
    if n%2 == 1 : 
        return x * (exp**2)
        

## Q2 ##

# returns the number of multiplications of a call to
# bin_pow(x,n)
def cost_bin_pow(n):
    if n <= 1 : 
        return 0 
    expression = cost_bin_pow(math.floor(n/2))
    
    if n % 2 == 0 : 
        return 1 + expression
    
    else : 
        return 2 + expression

## Q3 ##

# returns -1 if n is prime, and returns the smallest factor
# p>=2 of n if n is composite
def smallest_factor(n):
    for i in range(2, math.floor(math.sqrt(n))+1) :           
        if n % i == 0 :
            return i  
    return -1

## Q4 ##

# factorization powering, returns x^n
def factor_pow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x

    p = smallest_factor(n)

    if p == -1:
        return x * factor_pow(x, n - 1)

    else:
        q = n // p
        return factor_pow(factor_pow(x, p), q)
        
## Q5 ##

# returns the number of multiplications of a call to
# factor_pow(x,n)
def cost_factor_pow(n):
    
    if n <= 1 : 
        return 0 
    p = smallest_factor(n) 
    
    if p == -1 : 
        return 1 + cost_factor_pow(n-1) 
    
    else : 
        return cost_factor_pow(p) + cost_factor_pow(n//p)

## Q6 ##

# returns x^n from an addition chain of n (stored in the parameter chain)
def power_from_chain(x, L):
    dictio = dict() 
    
    for i in range(1,len(L)) :      
        target = L[i]
        dictio[L[i]] = [L[i-1]]
        
        for j in range(0,i) : 
            if L[i-1] + L[j] == target :
                dictio[L[i]].append(L[j])   
    powers = {1 : x}
    
    for cle,valeur in dictio.items() :         
        i,j = valeur
        powers[cle] = powers[i] * powers[j]
        
    return powers[L[-1]]
    
    
        

## Q8 ##

# returns the addition chain for n (path from the root
# to n in the power tree) after inserting enough
# layers of the tree so that n is part of it
arbre = PowerTree() 
def power_tree_chain(n):
    while n not in arbre.parent : 
        arbre.add_layer()
        
    tree_chain = arbre.path_from_root(n)
    
    return tree_chain

# power tree powering, returns x^n
def power_tree_pow(x, n):
    
    if n <= 0 : return 1
    
    L = power_tree_chain(n) 
    
    return power_from_chain(x,L)

## Q9 ##

# number of multiplications of a call to power_tree_pow(x,n)
# does not count the cost of building the tree
def cost_power_tree_pow(n):
    
    if n == 0 :
        return 0
    
    
    L = power_tree_chain(n)
    
    return len(L) - 1

# prints the compared costs
def compare_costs(m):
    for n in range(1, m + 1):
        print(
            n,
            cost_bin_pow(n),
            cost_factor_pow(n),
            cost_power_tree_pow(n)
        )