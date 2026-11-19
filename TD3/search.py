# -*- coding: utf-8 -*-

import math

def binary_search_rec(A,v,left,right):
    if (right >= left):
        mid = left + (right - left)//2 # using `(right + left)//2` can lead to an integer overflow
        if (v == A[mid]):
            return mid
        elif (v < A[mid]):
            return binary_search_rec(A,v,left,mid-1)
        else:
            return binary_search_rec(A,v,mid+1,right)
    
    return -1
        
## Q1 ##
def binary_search(A,v):
    
    n = len(A)
    l,r = 0, n-1
    
    while l <= r : 
        middle = (l+r)//2 
        
        m_value = A[middle]
        
        if v > m_value : 
            l=middle+1
            
        elif v < m_value : 
            r = middle-1
            
        else : 
            return middle
        
    return -1


# enfaite le pire cas c'est quand la valeur cherché est a l'extremité
# ou bien pas presente donc il faut qu'on ai plus qu'une seule valeur donc 
# n/(2^k) = 1 so k = log base 2 (n) donc sa c'est notre nombre de recursion max et pour chaque truc on divise par 

#### JE ME SUIS CASSE LA TETE JE PASSE PAR LA FONCTION RECURSIVE ET JE TROUVE QUE a =1 , b =2 

def cost_binary_search(n):
    if n <= 1 :
        return 1
    
    return cost_binary_search(math.ceil(n/2)) + 3
    
    
    
## Q2 ##
def ternary_search(A, v):
    l, r = 0, len(A) - 1

    while l <= r:
        a = l + (r - l) // 3
        b = r - (r - l) // 3

        if v == A[a]:
            return a
        elif v == A[b]:
            return b

        elif v < A[a]:
            r = a - 1

        elif v > A[b]:
            l = b + 1

        else:
            l = a + 1
            r = b - 1

    return -1

#ici c'est simple, enfaite on lance une recursion dans 1 des 3 cas et on divise par 3 le n, donc on a une recursion et divise par 3
def cost_ternary_search(n):
    if n <= 1:
        return 1

    return cost_ternary_search(math.ceil(n/3)) + 1
    
def cost_binary_search_value(A,v):
    # if len(A) == 0: return 1
    left = 0
    right = len(A) - 1

    cost = 1
    while (right >= left):
        mid = left + (right - left)//2
        cost += 1 
        if (v == A[mid]):
            return cost
        else: # decomposed elif into else if, then inserted "cost += 1" before the if
            cost += 1
            if (v < A[mid]):
                right = mid - 1
            else:
                left = mid + 1
        cost += 1

    return cost

def cost_ternary_search_value(A, v):
    l, r = 0, len(A) - 1

    cost = 1

    while l <= r:
        a = l + (r - l) // 3
        b = r - (r - l) // 3

        cost += 2

        cost += 1
        if v == A[a]:
            return cost

        cost += 1
        if v == A[b]:
            return cost

        cost += 1
        if v < A[a]:
            r = a - 1

        else:
            cost += 1
            if v > A[b]:
                l = b + 1
            else:
                l = a + 1
                r = b - 1

        cost += 1

    return cost


## Q3 ##
## ici j'aurais put utiliser la premiere que j'ai codé mais bon je voulais gagner du temps
def binary_search_2(A,v,left,right) : 
    
    l,r = left,right
    
    while l <= r : 
        middle = (l+r)//2 
        
        m_value = A[middle]
        
        if v > m_value : 
            l=middle+1
            
        elif v < m_value : 
            r = middle-1
            
        else : 
            return middle
        
    return -1
    
def exponential_search(A,v):
    
    k = 0 
    
    while 2**k < len(A) : 
        
        if v == A[2**k] : 
            return 2**k
        if v < A[2**k] : 
            break
        k+=1
    
    l = 2**(k-1)
    r = 2**(k)
    
    return binary_search_2(A,v,l+1,r-1)

def cost_exponential_search(v):
    
    # we need first to find, v so we have 2^k >= v > 2^k-1 so k = log(v)
    # then we are in [2^k-1,2^k] the lenght is 2^k-1
    # we need to count the computation for the exponential search and we start at 0 so k+1
    
    k = math.ceil(math.log2(v))
    return cost_binary_search(2**(k-1)) + k+1

## Q4 ##
def interpolation_search(A,v):
    
    l,r = 0,len(A)-1
    
    if len(A) == 0 : 
        return -1 
    
    if len(A) == 1 :
        if A[0] == v : 
            return 0
        return -1 
    
    # ici on verifie si juste il est pas dans l'array, psq on suppose que l'array est sorted. 
    if v < A[l] or v > A[r]:
        return -1
     
    # case where, we are going to devise by 0  so all the elemnts are the same   
    if A[l] == A[r] : 
        if A[l] == v : 
            return l
        else : 
            return -1
    
    k = l + (((v - A[l]) * (r-l)) //(A[r] - A[l]))
    
    if v < A[k] : 
        return interpolation_search(A[:k],v)
    
    elif v > A[k] : 
        
        # here we are goind to have a decalage d'indice, parce que je vais envoyer A[k+1]
        
        result = interpolation_search(A[k+1::],v) 
        
        # if there is no result we return -1 
        if result == -1 : 
            return -1
        
        return result + (k+1) # ici on ajoute le delage. 
    
    else : 
        return k 
    
    

## Q6 ##
def findFirstOccurrence(A, v):
    # enfaite si j'ai bien compris ce qu'on devrait faire c'est si on trouve v, on va cherhcher a sa gauche. 
    # pour voir si y'a un autre v si c'est -1 on sait qu'on doit return. 
    # et je pense qu'on doti pas gerer le decalge laisse moi voir
    
    first = -1    
    current = None 
    B = A.copy()
    
    while current != -1 : 
    
        
        k = binary_search(B,v)
        
        
        
        if first == -1 and k != -1 : 
            first = k 
        
        if k < first and k!=-1 : 
            first = k 
            
        current = k 
        
        if current == -1 : 
            break
            # pour ne pas faire B[:-1]
        
        B = B[:k] 
        
    return first 
        
    
    

def findLastOccurrence(A, v):
    # ici c'est interessant aussi enfaite on doit cherhchehrr a droite, mais attention je vais devoir 
    # regarder a droite cette fois dans je suis certain que je vais devoir prendre en compte un decalage des indices 
    
    last = 0 
    current = None 
    decalage = -1
    
    B = A.copy()
    
    while current != -1 : 
        
        #ici je prepare le decalage
        
        k = binary_search(B,v)
        
        if k != -1 : 
            decalage += 1 
            last += k 
            
        current = k 
        
        if current == -1 : 
            break
        
        B = B[k+1::]
        
    return last + decalage

## Q7 ##

    


def findKClosestElements(A, v, k):
    # on suppise que A est sorted, donc si c pmus petit que le min alors les k plus proches sont les k premers et meme
    # meme raisonnement pour les derniers

    if k == 0:
        return []

    if v <= A[0]:
        return A[:k]

    if v >= A[-1]:
        return A[-k:]

    l, r = 0, len(A) - 1

    while l <= r:

        middle = (l + r) // 2

        if A[middle] < v:
            l = middle + 1
        else:
            r = middle - 1

    # so now l = i , r=i+1
    left = r
    right = l

    resultat = []

    while len(resultat) < k:

        if left < 0:
            resultat.append(A[right])
            right += 1

        elif right >= len(A):
            resultat.insert(0, A[left])
            left -= 1

        else:
            distance_left = abs(A[left] - v)
            distance_right = abs(A[right] - v)

            if distance_left <= distance_right:
                resultat.insert(0, A[left])
                left -= 1

            else:
                resultat.append(A[right])
                right += 1

    return resultat
    

## Q8 ##

def findFrequency(A):
    
    #la c'est bcp plus simple, enfaite je vais rester diviser jusqua avoir un array qui ont que chacun le meme element 
    # et je met stack, qui est comme ma liste des taches. des intervalles que je vais verifier. 

    freq = {}

    if len(A) == 0:
        return freq

    stack = [(0, len(A) - 1)]

    while stack:

        l, r = stack.pop()

        if A[l] == A[r]:
            freq[A[l]] = freq.get(A[l], 0) + (r - l + 1)

        else:
            middle = (l + r) // 2

            stack.append((l, middle))
            stack.append((middle + 1, r))

    return freq



