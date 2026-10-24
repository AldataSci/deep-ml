def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			# Multiply each scalar entry to a matrix entry
			matrix[i][j] = matrix[i][j] * scalar

	return matrix