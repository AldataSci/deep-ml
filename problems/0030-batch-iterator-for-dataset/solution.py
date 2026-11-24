# Cell 1
import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    # Your code here
    # 1. Create an empty outer list..
    listr = []
    if y is not None:
        # Now we are going through the sliced values.. 
        for i, j in zip(range(0,len(X),batch_size),range(0,len(y),batch_size)):
            # Within the loop, slice both arrays from the current index
            
            # We append the sliced array together as a pair.. 
            listr.append([X[i:i+batch_size],y[j:j+batch_size]])
        return listr
    else:
        for i in range(0,len(X),batch_size):
            listr.append(X[i:i+batch_size])
        return listr
        
        # Return the y_batch