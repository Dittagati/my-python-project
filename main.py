import numpy as np

matrix = np.array([1, 2, 3, 4, 5, 7, 8, 8])
matrix_2 = np.array([[1, 2, 3], [1, 2, 3]])
x = matrix.copy()

matrix[0] = 42

print(x)
print(matrix)
print(matrix_2)

