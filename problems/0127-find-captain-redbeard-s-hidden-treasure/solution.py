# Cell 1
def find_treasure(start_x: float) -> float:
    """
    Find the x-coordinate where f(x) = x^4 - 3x^3 + 2 is minimized.

  Returns:
        float: The x-coordinate of the minimum point.
    """
    # Your code here
    steps = 1000
    learning_rate = 0.01
    momentum = 0.8
    velocity = 0
    
    for step in range(steps):
        # Find the slope i.e plug in x into the derivative.. which we manually input.. 
        slope = (4 * (start_x ** 3)) - (9 * (start_x ** 2))
        
        # Update the velocity with our momentum formula 
        # i.e the updated version of the update rule
        velocity = (momentum * velocity) - (learning_rate * slope)
        
        # Update our x or start_x in this case.
        start_x = start_x + velocity
    
    return start_x