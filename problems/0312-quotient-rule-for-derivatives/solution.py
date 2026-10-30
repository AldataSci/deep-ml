# Cell 1
import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    if len(g_coeffs) == 1:
        g_normal = g_coeffs[0]
        g_prime = 0
        
        h_normal = (h_coeffs[0] * x) + (h_coeffs[1])
        h_prime = h_coeffs[0]
        
    elif len(g_coeffs) == 2:
        # [1,0]
        g_normal = (g_coeffs[0] * x) + (g_coeffs[1])
        g_prime = g_coeffs[0]
        
        h_normal = (h_coeffs[0] * (x ** 2)) + (h_coeffs[1] * x) + (h_coeffs[2])
        h_prime = (2 * h_coeffs[0] * x) + (h_coeffs[1])
    elif len(h_coeffs) == 3:
        g_normal = (g_coeffs[0] * (x ** 2)) + (g_coeffs[1] * x) + (g_coeffs[2])
        g_prime = (2 * g_coeffs[0] * x) + (g_coeffs[1])
    # now we do h
        h_normal = (h_coeffs[0] * (x ** 2)) + (h_coeffs[1] * x) + (h_coeffs[2])
        h_prime = (2 * h_coeffs[0] * x) + (h_coeffs[1])
    
    # quotient rule.. just got to implement it correctly.. 
    elif len(h_coeffs) == 2:
        g_normal = (g_coeffs[0] * (x ** 2)) + (g_coeffs[1] * x) + (g_coeffs[2])
        g_prime = (2 * g_coeffs[0] * x) + (g_coeffs[1])
    # now we do h
        h_normal = (h_coeffs[0] * x) + (h_coeffs[1])
        h_prime = h_coeffs[0]
    
    # quotient rule.. just got to implement it correctly.. # it works! let's go
    quot = ((g_prime * h_normal) - (g_normal * h_prime)) / (h_normal ** 2)
    
    return quot