"""CSE202 mock midterm -- binary image compression. Complete Q1--Q5."""

def uniform_block(image, row, col, size):
    """Q1: return 0 or 1 if the block is uniform, else None."""
    
    white = 0 
    black = 0 
    
    for r in range(row,row+size) : 
        
        for c in range(col,col+size) : 
            
            if image[r][c] == 0 :
                white += 1 
            else : 
                black+= 1 
    
    if white > 0 and black == 0 : 
        return 0 
    elif black > 0 and white == 0 :
        return 1 
    return None


def encode(image):
    """Q2: build the canonical quadtree of a nonempty square image."""
    n = len(image)
    row,col = 0,0
    
    
    return encode_helper(image,row,col,n) 

def encode_helper(image,row,col,size) : 
    
    result = uniform_block(image,row,col,size) 
    
    if result is not None : 
        return result
    
    NW = encode_helper(image,row,col,size//2)
    NE = encode_helper(image,row,col + size//2,size//2)
    SW = encode_helper(image,row + size//2,col,size//2)
    SE = encode_helper(image,row + size//2 ,col + size//2,size//2)
    
    return (NW,NE,SW,SE)
        

def quadrant(row, col, size):
    mid = size // 2

    if row < mid:
        if col < mid:
            return 0
        else:
            return 1
    else:
        if col < mid:
            return 2
        else:
            return 3
    

def pixel(tree, size, row, col):
    """Q3: obtain a pixel without reconstructing the image."""
    
    relative_row = row
    relative_col = col   
    
    current = tree
    while  not isinstance(current,int) : 
        
        i = quadrant(relative_row,relative_col,size)
        current = current[i]
            
        if i == 1 :
            relative_col = relative_col - size//2
            
        if i == 2 :
            relative_row = relative_row - size//2
            
        if i == 3 : 
            relative_row = relative_row - size//2
            relative_col = relative_col - size//2
            
        size = size//2
        
            
    return current
            
        

def black_pixels(tree, size):
    """Q4: count 1-pixels without reconstructing the image."""
    
    count = 0 
    
    if isinstance(tree,int) : 
        if tree == 1 : 
            count += (size)**2 
        return count
            
    size = size//2 
    for i in tree : 
        count += black_pixels(i,size)
        
    return count



def decode_helper(tree, image, row, col, size):

    if tree == 0:
        return

    if tree == 1:
        for i in range(row, row + size):
            for j in range(col, col + size):
                image[i][j] = 1
        return

    half = size // 2

    decode_helper(tree[0], image, row, col, half)               # NW
    decode_helper(tree[1], image, row, col + half, half)        # NE
    decode_helper(tree[2], image, row + half, col, half)        # SW
    decode_helper(tree[3], image, row + half, col + half, half) # SE


def decode(tree, size):
    image = [[0] * size for _ in range(size)]

    decode_helper(tree, image, 0, 0, size)

    return image

# Q3: Explain briefly why the search visits at most log2(size) internal nodes.
# its height of the tree wich is log^2 ; 
