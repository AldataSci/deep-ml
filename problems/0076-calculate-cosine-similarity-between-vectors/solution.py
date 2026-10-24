import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if len(v1) == len(v2):
        # calculate dot product
		total = 0.0
		for i in range(len(v1)):
			prod = v1[i] * v2[i]
			total = total + prod
        
        # calculate norm..a
		norm_a = v1 ** 2
		norm_b = v2 ** 2
		
		norm_a_sum = norm_a.sum()
		norm_b_sum = norm_b.sum()
        
        # Calculate
		norm_a_sq = norm_a_sum ** (1/2)
		norm_b_sq = norm_b_sum ** (1/2)
	
	return total / (norm_a_sq * norm_b_sq)