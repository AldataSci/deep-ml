# Cell 1
import numpy as np

def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iter: int) -> list:
    """
    Perform n_iter steps of stochastic gradient descent on a linear regression
    model with MSE loss, cycling through samples in order.

    Returns the final weight vector as a Python list.
    """
    # Iterate through the # of n_iters
    for iters in range(n_iter):
        # then we use the modulo so that for each iteration i we pick out the samples iters % len(X)
        
        # Calculate the prediction.. 
        y_pred = np.dot(X[iters % len(X)],weights)
        
        # Now we calculate the error for those particular weights
        error = y_pred - y[iters % len(X)]
        
        # Do calculate the gradient which they gave as: find the derivative for the standard mse convention: (y_pred - y) ** 2 and the deriv is 2 * (error) x[iters% len(X)]
        gradient = 2 * X[iters % len(X)] * (error)
        
        # do the weight update rule: 
        weights = weights - (learning_rate * gradient)
        
    return weights
        
        # Calculate the error for that particular x value