# Cell 1
import numpy as np
from scipy.special import expit
def train_neuron(features: np.ndarray, labels: np.ndarray, int_weights: np.ndarray, int_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    # Your code here
    mse_avg = []

    for epoch in range(epochs):
    # We need a new predcitons list for every epoch.. ohh cause we are using the updated weights..
        predictions = []
        for i in range(len(features)):
            total = 0.0
            for j in range(len(int_weights)):
        # Walk across the features row by row and multiply it by the weights
                prod = features[i][j] * int_weights[j]
                total = total + prod
    # We get out of the loop to add the bias in
            total = total + int_bias
    # Oh yeah we need the sigmoid i forget
            sigmoid = expit(total)
            predictions.append(sigmoid)

#print(predictions)

# Calculate the loss (MSE)

        mse_total = 0
# Ds stands for derivative of sigmoid
        ds = []
# derivative of loss
        dl = []
        for y,y_prime in zip(labels,predictions):
            diff = y_prime - y
    # Now we square it
            diff_sq = (diff) ** 2
    # We sum the mse
            mse_total = mse_total + diff_sq
    
    # Now calculate avg
            ds.append(2 * (diff))
            dl.append(y_prime * (1 - y_prime))
        avg = mse_total / len(labels)
        mse_avg.append(avg)
    # Oh yeah i could do it here then
    #ds.append(2 * (diff))
    

# Step 3 loss backawards step step

#for 
#deriv_of_loss = 2 * (predictions - labels)
#deriv_of_sigmoid = predictions * (1 - predictions)

#delta = deriv_of_loss * deriv_of_sigmoid

# Oh yeah we could do that.. I hate that i am jobless lmfao

# Now we do the individual calculations.. we find the delta

        delta = []

        for i in range(len(ds)):
            delta.append(ds[i] * dl[i])
    
#print(delta)

# Now we assign blames.. to the weight and biass.

# We use the three deltas to calculate the average nudge needed for each weight and bias

# Weight 1 gradient..
# Multiply each sample's feature by the first gradient
# Is this batch gradeitn descent.. 
        total1 = 0
        for i in range(len(features)):
    # This prints out the first value for every sample.. 
            total1 = total1 + (features[i][0] * delta[i])

        first_grad_vector_avg1 = total1/len(features)

#print(first_grad_vector_avg1)

        total2 = 0
        for i in range(len(features)):
    # We multiply by it by the second values in the features
            total2 = total2 + (features[i][1] * delta[i])

        second_grad_vector_avg2 = total2/len(features)

#print(second_grad_vector_avg2)

        bias1 = 0

        for i in range(len(delta)):
            bias1 = bias1 + delta[i]

        avg_bias = bias1/len(features)
    
#print(avg_bias)

# So we just calculated the average nudges for each weight and bias.. 

# Update the weight and bias by a nudge.. (the learning_rates..)

        int_weights[0] = int_weights[0] - (learning_rate * first_grad_vector_avg1)

        int_weights[1] = int_weights[1] - (learning_rate * second_grad_vector_avg2)

        int_bias = int_bias - (learning_rate * avg_bias)
    return int_weights, int_bias, mse_avg