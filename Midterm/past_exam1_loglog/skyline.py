# -*- coding: utf-8 -*-
"""CSE202 — Skyline midterm blanc. Complete the five functions.

Buildings: (left, height, right)
Skyline: ordered (left, height) pairs, ending at height 0.
Run tests with: python3 test_skyline.py
"""


def rects_height_at(rects, x):
    """Q1 (1 pt): maximum height at position x, with left <= x < right. O(n)."""
    
    resultat = 0
    
    for bat in rects : 
        left = bat[0]
        right = bat[2]
        height = bat[1]
        
        if left <= x and x < right : 
            if height > resultat : 
                resultat = height 
    return resultat

sky1_red = [(1,11),(2,11),(3,13),(5,13),(7,13),(9, 0),(12,7),(14,7),(16, 3),
(19,18),(22,3),(23,13),(24,13),(25,13),(28,13),(29,0)]


def simplify_skyline(skyline):
    """Q2 (1 pt): remove consecutive strips of equal height. O(n)."""
    
    resultat = []
    
    for i in range(len(skyline)) : 
        
        if i == 0 : 
            resultat.append(skyline[i])
            continue
        
        left,height = skyline[i]
        
        if height != resultat[-1][1] : 
            resultat.append(skyline[i])
            
    return resultat
        


def skyline_naive(rects):
    """Q3 (2 pts): minimal skyline of rectangles in O(n**2)."""
    X_L = set()
    
    for bat in rects : 
        
        l,h,r = bat 
        
        X_L.add(l)
        X_L.add(r)
        
    X_L = sorted(list(X_L))
    sky = []
    for i in range(len(X_L)) : 
        if i == 0 : 
            
            sky.append((X_L[i],rects_height_at(rects,X_L[i])))
            continue
        
        
        else : 
            sky.append((X_L[i],rects_height_at(rects,X_L[i])))
            
            
            
    return simplify_skyline(sky)
    


def merge_skylines(sky1, sky2):
    """Q4 (4 pts): merge two minimal skylines in O(len(sky1)+len(sky2))."""

    h1 = 0 
    h2 = 0
    
    i1 = 0
    i2 = 0
    
    S = []
    
    while i1 < len(sky1) and i2 < len(sky2) : 
        
        
        
        
            
        bat1 = sky1[i1]
        bat2 = sky2[i2]
        
        if bat1[0] < bat2[0] : 
            h1 = sky1[i1][1]
            S.append((bat1[0],max(h1,h2)))
            i1 += 1 
        elif bat1[0] > bat2[0] : 
            h2 = sky2[i2][1]
            S.append((bat2[0],max(h1,h2)))
            i2 += 1
        else : 
            h2 = sky2[i2][1]
            h1 = sky1[i1][1]
            
            S.append((bat1[0],max(h1,h2)))
            i1 += 1 
            i2 += 1
            
    if i1 == len(sky1) : 
        S = S + sky2[i2::]
        
    else : 
        S = S + sky1[i1::]
        
    return simplify_skyline(S)
            


def skyline_dac(rects):
    """Q5 (2 pts): divide-and-conquer skyline in O(n log n)."""
    
    if len(rects) <= 1 : 
        return skyline_naive(rects)
    
    mid = len(rects)//2 
    left_half = rects[:mid]
    right_half = rects[mid:]
    
    sorted_left = skyline_dac(left_half)
    sorted_right = skyline_dac(right_half)
    
    return merge_skylines(sorted_left,sorted_right)
