# Cell 1
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == 'column':
        listr = [] 
        for col in range(len(matrix[0])):
            sum = 0
            for row in range(len(matrix)):
        # The column stays the same the row changes
        # okay
                sum = sum + matrix[row][col]
    
            avg = sum / len(matrix)
            listr.append(avg)
        return listr
    
    elif mode == 'row':
        listr = []
        for row in range(len(matrix)):
            sum = 0 
            for col in range(len(matrix[0])):
                sum = sum + matrix[row][col]
    
            avg = sum / len(matrix[0])
            listr.append(avg)
        return listr