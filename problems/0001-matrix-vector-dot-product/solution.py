def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(a[0]) != len(b):
		return -1
	listr = []
    # Go thorugh each entry in the matrix
	for row in a:
		total = 0
		for j in range(len(row)):
			prod = row[j] * b[j]
			total = total + prod
		listr.append(total)
	return listr