# Cell 1
import numpy as np
from scipy.special import expit

def digit_network_forward(image, weights, biases):
    """Run an image through a fully connected sigmoid network.

    Returns (output activations rounded to 4 decimals, predicted digit).
    """
    # First we flatten it the 2d image grid into a single flat line of number
    # Current_input contains the flatten version of our image values..
    
    current_image = []
    for row in image:
        for pixel in row:
            current_image.append(pixel)
    
    # The next step is setting up a loop that goes through your layer one at a time.
    for i in range(len(weights)):
        layer_w = weights[i]
        layer_b = biases[i]
        next_inputs = []
        
        # Now we go through the neurons within that particular hidden layer.
        for j in range(len(layer_w)):
            # Now we access the neurons..
            total = 0.0
            # We now multiply and then sum it with the current inputs
            for k in range(len(current_image)):
                # We go across each layer row by row values and multiply it with current_inputs
                prod = layer_w[j][k] * current_image[k]
                total = total + prod
            # After the computation we add the biase value now
            total = total + layer_b[j]
            
            # Now we apply the sigmoid function..
            next_inputs.append(expit(total))
        
        # Now our current image containes the next inputs.. 
        current_image = next_inputs
    # Return the current next inputs and the argmax positions..         
    return (next_inputs,current_image.index(max(current_image)))