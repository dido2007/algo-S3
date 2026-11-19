# -*- coding: utf-8 -*-

class PowerTree:
    
  # constructor, initializes the tree with a single node (the root 1)
  # and a single layer (layer 0, containing the root node)  
    def __init__(self): 
        self.layers=[[1]]
        self.parent={1:1}
    
  # displays the layers of the tree
    def draw_tree(self):
        for i in range(len(self.layers)):	
            print("layer",i)
            for j in self.layers[i]: print(j,"->",self.parent[j])  
  	
  # if k is not in the tree (not enough layers built) return -1
  # if k is in the tree, returns a list giving the successive labels
  # on the path from the root (equal to 1) to k
    def path_from_root(self,k):
        if k not in self.parent.keys() : return -1
        
        current = k 
        path = []
        
        while current != 1 : 
          path.insert(0,current)
          current = self.parent[current]
        
        path.insert(0,1)
        
        return path
    
  # adds the (k+1)th layer to the tree, when the layers
  # already in the tree are 0..k  
    def add_layer(self):
        
        layer = self.layers[-1]
        
        next_layer = []
        
        for j in layer : 
          path = self.path_from_root(j)
          
          for i in path : 
            if j+i not in self.parent : 
              next_layer.append(j+i)
              self.parent[j+i] = j
        self.layers.append(next_layer)
              
        
