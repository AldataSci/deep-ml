# Cell 1
def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
    # Return the element-wise sum of vectors 'a' and 'b'.
    # If vectors have different lengths, return -1.
    
    listr = []
    if len(a) == len(b):
        for i in range(len(a)):
            sum = a[i] + b[i]
            listr.append(sum)
        return listr
    return -1