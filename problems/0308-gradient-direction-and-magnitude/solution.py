# Cell 1
import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.
    
    Args:
        gradient: A list representing the gradient vector
    
    Returns:
        Dictionary containing:
        - magnitude: The L2 norm of the gradient
        - direction: Unit vector in direction of steepest ascent
        - descent_direction: Unit vector in direction of steepest descent
    """
    # Your code 
    # if gradient is the zero vector then..
    if all(x == 0 for x in gradient):
        return {'magnitude': 0, 'direction': [0] * len(gradient), 'descent_direction': [0] * len(gradient)}
        
    sum = 0
    for grad in gradient:
        squared = grad ** 2
    # sum up the components
        sum = sum + squared
        root = sum ** (1/2)
    # print(root)

## Calculate descent

    norm = list()
    descent = list()
    for d in gradient:
        normal = d/root
        norm.append(normal)
    
    # also calculate descent_dir
        descent.append(-1 * normal)
    
    return {'magnitude': root, 'direction': norm, 'descent_direction': descent}