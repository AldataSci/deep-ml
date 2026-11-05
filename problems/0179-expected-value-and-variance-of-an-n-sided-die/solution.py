# Cell 1
def dice_statistics(n: int) -> tuple[float, float]:
    """
    Compute the expected value and variance of a fair n-sided die roll.

    Args:
        n (int): Number of sides of the die

    Returns:
        tuple: (expected_value, variance)
    """
    # Your code here
    expected_value = 0
    variance = 0
    for i in range(1,n+1):
        expected_value = expected_value + (i * (1/n))
    
    variance = ((n**2) - 1) / 12
    return (expected_value, variance)