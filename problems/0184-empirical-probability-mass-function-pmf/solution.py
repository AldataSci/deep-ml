# Cell 1
from collections import defaultdict

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    Hash = defaultdict(int)
    listr = [] 
    
    # we do this to count the # of occurences.. 
    for c in samples:
        Hash[c] += 1
    
    for key,value in Hash.items():
        k = key
        probability = value / len(samples)
        # Append the tuple into a list
        listr.append((k,probability))
    
    return listr