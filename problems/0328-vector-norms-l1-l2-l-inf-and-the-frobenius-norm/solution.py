import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    if norm_type == 'l1':
        # convert it to absolute norm..
        # Place it in a numpy array so that you can properly flatten it
        norm_abs = np.array([abs(x) for x in arr])
        
        norm_flat = norm_abs.flatten()
        
        # Do it the good old way..
        total = 0.0
        for i in norm_flat:
            total = total + i
        # Return the total of the absolute values of the entries in the matricies..
        return total
    
    # Try L2 norm
    elif norm_type == 'l2':
        # L2 norm is square root of the sum of the squared entries so..
        
        abs_norm_l2 = np.array([abs(x) for x in arr])
        
        # We have to make sure to flatten the array into a one-dim matrix.. but works on np.array
        abs_norm_flat = abs_norm_l2.flatten()
        
        # Now take the sum of the squared entries
        total = 0.0
        for i in abs_norm_flat:
            total = total + (i ** 2)
        
        return total ** (1/2)
    
    elif norm_type == 'linf':
        
        # Enclose it in a numpy array
        abs_l3 = np.array([abs(x) for x in arr])
        
        # Make it a flat array.. to handle 2-d array.. 
        abs_flat = abs_l3.flatten()
        
        # Now take the max value
        mmax = 0.0
        
        for i in abs_flat:
            if mmax < i:
                mmax = i
        
        return float(mmax)
        
    
    
    elif norm_type == 'frobenius':
        if arr.ndim != 2:
            raise ValueError(f"Input must be a 2-d array, but got a {arr.ndim} dim array")
    # Then do the normal calculation as usual..
    # Square all the entry in the matrix
        arr_sq = arr ** 2
    
    # Then sum and then take square root 
    
        arr_sum = arr_sq.sum()
    
    # Then take the square root
    
        arr_root = arr_sum ** (1/2)
    
        return arr_root
    
    else:
        raise ValueError(f'Please enter norm_type')