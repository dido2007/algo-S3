import math
import random
import copy

## Question 5 ##


def random_element(dict):
    # TO COMPLETE
    
    total_weights = sum(dict.values())
    
    sequences = []
    weights = []
    
    for cle,valeur in dict.items() : 
        sequences.append(cle)
        weights.append(valeur/total_weights)  
    
    return random.choices(sequences,weights,k=1)[0]

## Question 7 ##


def random_cut(m):
    # TO COMPLETE
    M = copy.deepcopy(m)
    partition = {cle:[] for cle in M.deg.keys()}
    
    while len(M.deg) > 2 : 
        
        a,b = M.random_edge()    
        
        M.contract(a,b)
        
        partition[a] += partition[b] + [b]
        
        del partition[b]
        
    a = next(iter(M.deg)) 
    
    return [M.deg[a], [a] + partition[a]]
    
        
    
        
        
        


def mincut_karger(L, p):
    n = L[0]

    r = 0
    minimum = None

    failure_bound = 1 - 2 / (n * (n - 1))

    while failure_bound**r > p:

        M = MultiGraph(L)
        cut = random_cut(M)

        if minimum is None or cut[0] < minimum[0]:
            minimum = cut

        r += 1

    return minimum
        

## Contains Questions 4 and 6 ##


class MultiGraph:
    def __init__(self, L):
        self.adj = {}
        self.deg = {}
        for x in L[1]:
            if x[0] not in self.adj:
                self.adj[x[0]] = {x[1]: x[2]}
                self.deg[x[0]] = x[2]
            else:
                self.adj[x[0]][x[1]] = x[2]
                self.deg[x[0]] += x[2]
            if x[1] not in self.adj:
                self.adj[x[1]] = {x[0]: x[2]}
                self.deg[x[1]] = x[2]
            else:
                self.adj[x[1]][x[0]] = x[2]
                self.deg[x[1]] += x[2]

    # i is an integer between 1 and 2^n - 2, with n the number of vertices
    def subset_from_integer(self, i):
        subset = {}
        for x in self.adj:
            if i % 2 == 1:
                subset[x] = True
            i = i >> 1
        return subset

    def cutsize(self, i):  # i is an integer between 1 and 2^n - 2, with n the number of vertices
        subset = self.subset_from_integer(i)
        res = 0
        for x, y in self.adj.items():
            for t, u in y.items():
                if x in subset and not t in subset:
                    res += u
        return [res, [x for x in subset]]

    def display(self):
        for x, y in self.adj.items():
            print("Neighbors of " + str(x) +
                  ", which has degree " + str(self.deg[x]))
            for t, u in y.items():
                print(str(t) + " with multiplicity " + str(u))

    ## Question 4 ##
    def contract(self, i, j):  # contracts edge i, j (i absorbs j)
        
        self.deg[i] += (-self.adj[j][i] + (self.deg[j] - self.adj[j][i])) # a simplfier ?  
        
        # je supprime les correspondance
        del self.adj[j][i]
        del self.adj[i][j]
        
        #je suppriùe le deg de j psq il est effacé
        del self.deg[j]
        
        for (y,n) in self.adj[j].items() : 
            
            #j'ajoute les voisions vers i
            self.adj[i][y] = self.adj[i].get(y,0) + n 
            
            # j'efface j des ses voisins, et je les rajoutes a i
            self.adj[y][i] = self.adj[y].get(i,0) + self.adj[y].pop(j)
            
        del self.adj[j]
            
            
            
            


    ## Question 6.1 ##
    def random_vertex(self):

        return random_element(self.deg)

    ## Question 6.2 ##
    def random_edge(self):

        i = self.random_vertex()
        
        j = random_element(self.adj[i])
        
        return (i,j)
