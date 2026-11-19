#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

# import numpy as np
A =  [[3, -1, 2], [0, 2, 0], [-2, 1, 3]]
B =  [[3, -1, 2], [0, 2, 0], [-2, 1, 3]]

#Q6
def mult_matrix(A,B):
    result = []
    for i in range(len(A)) :  
        temp = []   
        for j in range(len(B[0])) :
            c = 0 
            for k in range(len(A)) : 
                
                c += A[i][k] * B[k][j]
            temp.append(c)
            
        result.append(temp)
            
    return result
            
        
            
             
            
            
# ici c'est simple je vois que je fais quand n = 3 ; 3 multiplicatiosn et 2 additions, sa je le fait fait n fois 
# puis encore n fois donc n^3 + n^2(n-1)

#Q7
def cost_mult_matrix(n):
    if n == 1 : 
        return 1 
    
    if n == 2 : 
        return 12 
    
    return n**3 + (n**2)*(n-1)
    
    

#Functions split, merge, add_matrix and sub_matrix are given
def split(A):
    row, col = len(A), len(A[0])
    row2, col2 = row//2, col//2
    return [A[i][:col2] for i in range(row2)], [A[i][col2:] for i in range(row2)], [A[i][:col2] for i in range(row2,row)], [A[i][col2:] for i in range(row2,row)]

def merge(a,b,c,d):
    return list(map(lambda e : e[0]+e[1], zip(a,b))) + list(map(lambda e : e[0]+e[1], zip(c,d)))

# def split(A):
#    A=np.array(A)
#    row, col = A.shape
#    row2, col2 = row//2, col//2
#    return A[:row2, :col2].tolist(), A[:row2, col2:].tolist(), A[row2:, :col2].tolist(), A[row2:, col2:].tolist()

#def merge(a,b,c,d):
#    return np.vstack((np.hstack((a, b)), np.hstack((c, d)))).tolist()

#Computes the matrix A+B
def add_matrix(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
                C[i][j] = A[i][j] + B[i][j]
    return C


#Computes the matrix A-B
def sub_matrix(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
                C[i][j] = A[i][j] - B[i][j]
    return C

#Q8
def strassen(A,B):
    if len(A) == 1 or len(B) == 1 : 
        return mult_matrix(A,B)
    
    a,b,c,d = split(A)
    x,y,z,t = split(B)
    
    q1 = strassen(a,add_matrix(x,z))
    q2 = strassen(d,add_matrix(y,t))
    q3 = strassen(sub_matrix(d,a),sub_matrix(z,y))
    q4 = strassen(sub_matrix(b,d),add_matrix(z,t))
    q5 = strassen(sub_matrix(b,a),z )
    q6 = strassen(sub_matrix(c,a),add_matrix(x,y))
    q7 = strassen(sub_matrix(c,d),y)
    
    return merge(add_matrix(q1,q5),add_matrix(add_matrix(q2,q3),sub_matrix(q4,q5)),add_matrix(add_matrix(q1,q3),sub_matrix(q6,q7)), add_matrix(q2,q7))

#there is 7 recurise call and each they give a matrix of lenght (n/2)
# and in the renturn we have 8 operations and for the recurisive calls we have 10 additons 
# so 18 calls in the fonction, and they are all of leghts (n/2)^2 
# so we have : T(n) = 7*T(n/2) + 18*(n/2)^2
# but here our function is with k and n = 2^k
# so we define C(k) = T(2^k) so C(k) = 7*C(k-1) + 18*(2^(k-1))^2
#Q9
def cost_strassen(k):
    if k == 0:
        return 1

    return 7 * cost_strassen(k-1) + 18 * (2**(k-1))**2
    

# B = [[1,2,3], [2,3,4], [5,6,7]]
#Q10
def convert_01(A):
    B = []
    
    for ligne in range(len(A)) : 
        temp = []
        for colonne in range(len(A[0])) : 
            if A[ligne][colonne] > 0 : 
                temp.append(1)
            else : 
                temp.append(0)
        B.append(temp)
    return B 

#Q11
def transitive_closure(A):
    
    M = convert_01(A)
    
    Id = []
    
    for i in range(len(A)) : 
        temp = []
        for j in range(len(A)) : 
            
            if i == j : 
                temp.append(1)
            else : 
                temp.append(0)
        Id.append(temp)
        
    M_Id = convert_01(add_matrix(Id,M))
    
    result = Id
    
    def bin_pow(x, n):
        if n == 0 : 
            return Id
        if n == 1 : 
            return x 
    
        exp = bin_pow(x,math.floor(n/2))
        if n % 2 == 0 : 
            return convert_01(strassen(exp,exp))
        if n%2 == 1 : 
            return convert_01(strassen(x,convert_01(strassen(exp,exp)))) 
    
    
    

    return bin_pow(M_Id,len(A)-1)





