import numpy as np

N = int(input())
matrix = []

for _ in range(N):
    row_as_strings = input().split()
    row_as_floats = list(map(float, row_as_strings))
    matrix.append(row_as_floats)

determinant = np.linalg.det(matrix)
print(round(determinant, 2))

        

        

    
    
