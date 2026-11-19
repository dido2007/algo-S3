# -*- coding: utf-8 -*-

### For comparing strings

def string_compare(P,S):
    for j in range(len(P)):
        if not P[j] == S[j]:
            return False
    return True


### naive string matcher
def string_match(T, P):
    
    if len(P) > len(T) : 
        return []
    if len(P) == len(T) and P[0] != T[0] : 
        return []
    
    resultat = []
    for i in range(len(T) - len(P) + 1) : 
        
        complete = True
        for j in range(len(P)) : 
            if P[j] != T[i+j] :
                complete = False 
                break
        if complete : 
            resultat.append(i)
            
    return resultat

### number of characters
base = 256

### karp_rabin_sum

def hash_string_sum(S):
    
    return sum([ord(i) for i in S])

def hash_string_sum_update(h, Ti, Tim):
    
    return h - ord(Ti) + ord(Tim)

def karp_rabin_sum(T,P):
    
    if len(P) > len(T) : 
        return []
    if len(P) == len(T) and P[0] != T[0] : 
        return []
    
    
    goal = hash_string_sum(P)
    resultat = []
    h = None
    spurious = 0
    for i in range(0,len(T) - len(P)+1) :
        if h is None : 
            h = hash_string_sum(T[:len(P)])
            
        if h == goal :     
            if P == T[i:i+len(P)] : 
                resultat.append(i)
            else : 
                spurious += 1 
        if i < len(T) - len(P):
            h = hash_string_sum_update(h, T[i], T[i + len(P)])        
        
    return (resultat,spurious)
        

### karp_rabin_mod

def hash_string_mod(S, q):
    
    h = 0 
    
    for c in S : 
        h = (h* base + ord(c)) % q
        
    return h 
        
    
def hash_string_mod_update(h, Ti, Tim, q, dm):
    
    result = ( base*( h - ((dm )*ord(Ti)) )  + ord(Tim) ) % q
    
    return result


def karp_rabin_mod(T,P, q):
    if len(P) > len(T) : 
        return []
    if len(P) == len(T) and P[0] != T[0] : 
        return []
    
    goal = hash_string_mod(P,q)
    resultat = []
    h = None
    spurious = 0
    dm = (base**(len(P)-1)) % q
    for i in range(0,len(T) - len(P)+1) : 
        if h is None : 
            h = hash_string_mod(T[:len(P)],q)
            
        if h == goal : 
            if P == T[i:i+len(P)] : 
                resultat.append(i)
            else : 
                spurious += 1 
        if i < len(T) - len(P):
            h = hash_string_mod_update(h, T[i], T[i + len(P)],q,dm)
            
    return (resultat,spurious)
