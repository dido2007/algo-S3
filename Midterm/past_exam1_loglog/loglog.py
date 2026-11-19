"""CSE202 — Midterm blanc : LogLog.

Complete les fonctions ci-dessous. Lance ensuite : python3 test_loglog.py
"""

import math
import hashlib


def bin_hash(x):
    """Given: deterministic 32-bit binary hash of x."""
    hash_object = hashlib.sha1(str(x).encode('utf-8'))
    hexa = hash_object.hexdigest()
    bina = bin(int(hexa, 16))[2:].zfill(160)[:32]
    return bina


### CODE TO BE COMPLETED

def cardinality(tab):
    """Q1 (2 pts): number of distinct elements in tab, in linear time."""
    
    result = set()
    
    for i in tab : 
        result.add(i)
        
    return len(result)
    


def bucket(bina, b):
    """Q2 (1 pt): integer represented by the first b bits of bina."""
    
    bucket = bina[:b]
    
    
    result = 0
    
    for i in range(len(bucket)) : 
        result += int(bucket[i]) * 2**(len(bucket) - i - 1)
        
    return result



def zeros(bina, b):
    """Q2 (1 pt): number of consecutive zero bits starting at position b."""
    
    maximum = 0 
    current = 0 
    
    for i in bina[b:] : 
        if i == "0" :
            current +=1 
            
        if i == "1" : 
            break
            
    return current

def sketch(L, b):
    """Q3 (2 pts): list of 2**b bucket size-indicators (0 if empty)."""
    
    dictio = {}
    
    for val in L : 
        
        h = bin_hash(val)
        
        buc = bucket(h,b)
        
        zer = zeros(h,b)
        
        if buc not in dictio : 
            dictio[buc] = zer + 1 
            
        else : 
            dictio[buc] = max(dictio[buc],zer + 1)
            
    m = 2**b 
    resultat = []
    
    for i in range(m) : 
        resultat.append(dictio.get(i,0))
        
    return resultat


def constant(b):
    """Given: adjustment coefficient for the LogLog estimator."""
    if b == 4:
        return 0.673
    elif b == 5:
        return 0.697
    elif b == 6:
        return 0.709
    else:
        return 0.7213 / (1 + 1.079 / 2**b)


def loglog(L, b):
    """Q4 (2 pts): harmonic-mean LogLog cardinality estimate."""
    
    somme = 0 
    bucket_index = sketch(L,b)
    
    m = 2**b 
    
    for i in range(m) : 
        somme += 2**(-bucket_index[i])
    
    return constant(b) * ((m**2)/somme)


def loglog_small_range_correction(L, b):
    """Q5 (2 pts): LogLog estimate with the small-range correction."""
    
    E = loglog(L,b)
    m = 2**b
    
    if E > (5*m)/2 : 
        return E
    
    bucket_index = sketch(L,b)
    
    V = 0 
    
    for i in bucket_index : 
        if i == 0 : 
            V += 1 
            
    if V : 
        return m * math.log(m/V)
    
    return E