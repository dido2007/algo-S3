# Question 1

import math


def middleL(n, i, j, a, b):

    m1_x = i + 2**(n-1) - 1
    m1_y = j + 2**(n-1) - 1
    
    # enfaite le centre quand on prend l'exemple de n = 2, on voit qu'on peut le calculer comme sa psq comme c tjr pair 
    # donc on a juste a prendre i + 2^n-1 qui est le debut de la 2eme moitié

    X = [
        (m1_x, m1_y),
        (m1_x+1, m1_y),
        (m1_x, m1_y+1),
        (m1_x+1, m1_y+1)
    ]

    minimum = math.inf
    index = None

    for k in range(len(X)):
        if math.dist(X[k], (a,b)) < minimum:
            minimum = math.dist(X[k], (a,b))
            index = k

    X.pop(index)
    
    return X

# Question 2
def lower_left_hole(n, i, j, a, b): # returns the coordinates of the hole of the lower left quadrant
    
    M = middleL(n,i,j,a,b)
    
    # ici c'est simple juste je vois si l'extremité est dans middle sinon je return l'extremité car c'est un hole grace a middle
    
    if (i+2**(n-1) - 1, j + 2**(n-1) - 1) not in M : 
        return (a,b)
    
    return  (i+ 2**(n-1) - 1, j + 2**(n-1) - 1)

def lower_right_hole(n, i, j, a, b): # returns the coordinates of the hole of the lower right quadrant
    
    M = middleL(n,i,j,a,b)
    
    # je devais faire attention psq j on a encore - 1 puisque dans les j on est pas monté dans le 2eme cadrant
    if (i+2**(n-1), j + 2**(n-1) - 1) not in M : 
            return (a,b)
  
    return (i+ 2**(n-1), j + 2**(n-1) - 1)

def upper_left_hole(n, i, j, a, b): # returns the coordinates of the hole of the upper left quadrant
    M = middleL(n,i,j,a,b)
    
    if (i+2**(n-1) -1, j + 2**(n-1) ) not in M : 
        return (a,b)
    
    return (i+2**(n-1) -1, j + 2**(n-1) )

# en gros a chaqque fois je dois check quel cse je vais verifier c'est tout 

def upper_right_hole(n, i, j, a, b): # returns the coordinates of the hole of the upper right quadrant
    M = middleL(n,i,j,a,b)
        
    # je devais faire attention psq j on a encore - 1 puisque dans les j on est pas monté dans le 2eme cadrant
    if (i+2**(n-1), j + 2**(n-1) ) not in M : 
        return (a,b)
      
    return (i+ 2**(n-1), j + 2**(n-1) )

# Question 3
def tile(n, i, j, a, b): # returns a list with a valid L-tiling of the punctured grid of type (n, i, j, a, b)
    
    # au debut je commence par ma base cae : 
    
    if n == 0 : 
        return []
    
    tiles = []
    
    # ajouter le middle
    
    middle = middleL(n,i,j,a,b)
    
    tiles.append(middle)
    
    # decomposer en 4 (on prend les holes)
    quad_lower_left = lower_left_hole(n, i, j, a, b)
    
    quad_lower_right = lower_right_hole(n, i, j, a, b)
    
    quad_upper_left = upper_left_hole(n, i, j, a, b)
    
    quad_upper_right = upper_right_hole(n, i, j, a, b)
    
    # appeller recurisvement 
    
    quad_lower_left_recur = tile(n-1,i,j,quad_lower_left[0],quad_lower_left[1])
    quad_lower_right_recur = tile(n-1,i + 2**(n-1),j,quad_lower_right[0],quad_lower_right[1])
    quad_upper_left_recur = tile(n-1,i,j + 2**(n-1),quad_upper_left[0],quad_upper_left[1])
    quad_upper_right_recur = tile(n-1,i+ 2**(n-1),j + 2**(n-1),quad_upper_right[0],quad_upper_right[1])
    
    # ici j'ai rajotué extend ( un peu grace a chat mais je connaisiaias pas l'utilisé de cette fonciton uen fois que j'ai compris c totalement logique.)
    tiles.extend(quad_lower_left_recur)
    tiles.extend(quad_lower_right_recur)
    tiles.extend(quad_upper_left_recur)
    tiles.extend(quad_upper_right_recur) 
    
    return tiles
    
    
    
    
