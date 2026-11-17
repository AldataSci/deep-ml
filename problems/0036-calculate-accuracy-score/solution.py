# Cell 1
import numpy as np

def accuracy_score(y_true, y_pred):
    # Your code here
    
    # Define the variables locally
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    
    for y,y_prime in zip(y_true,y_pred):
        if y == 1 and y_prime == 1:
            TP = TP + 1
        elif y == 1 and y_prime == 0:
            # Predicted negative but it is actually positive
            FN = FN + 1
        elif y == 0 and y_prime == 0:
            # Predicted negative and it is actually negative.
            TN = TN + 1
        elif y == 0 and y_prime == 1:
            # Actually negative but it is actually positive
            # False positive
            FP = FP + 1
     # Define total
    total = (TP + TN + FN + FP)
    true = (TP + TN)

    return true/total