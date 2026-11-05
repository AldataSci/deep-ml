# Cell 1
import numpy as np

from collections import defaultdict

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    # let's do mean
    sum = 0
    for i in data:
        sum = sum + i
    avg1 = sum / len(data)
    
    # now calculate the median
    if len(data) % 2 == 1:
        middle = data[len(data) // 2]
        #middle1 = data[len(data) // 2]
        #return middle
    
    elif len(data) % 2 == 0: # odd condition.
        # An even length list has two middle elements..
        right_mid = data[len(data) // 2]  # right index
        left_mid = data[(len(data) // 2) - 1] # left index 
        # now we calculate the mean 
        total = right_mid + left_mid
        middle = float(total / 2)
        #middle1 = data[len(data) // 2]
        #return middle
    
    #

    Hash = defaultdict(int)
    for c in data:
        Hash[c] += 1 

        max_val = max(Hash.values())

        top_keys = [k for k,v in Hash.items() if v == max_val]

    # Print it like this get to the list comprehension out lmao.. 
    # return top_keys[0]
    
    
    sum = 0
    for i in data:
        sum = sum + i
        avg = sum / len(data)

    # Subtract the mean? and square it

    sub = [(i - avg) ** 2 for i in data]

    # now we add it the squared differences?

    # and divide by the population variance
    summ = 0
    for i in sub:
        summ = summ + i
    
    variance = summ / len(sub)

    # calculate the percentiles..
    
    p25,p50,p75 = np.percentile(data,[25,50,75])
    
    return {'mean': avg, 'median': middle, 'mode': top_keys[0], 'variance': variance, 'standard_deviation': variance ** (1/2), '25th_percentile' : p25, '50th_percentile': p50, '75th_percentile': p75, 'interquartile_range': p75-p25 }