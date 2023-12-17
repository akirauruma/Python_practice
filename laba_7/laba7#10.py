import numpy as np

# 10x10 matrix
matrix = np.zeros((10, 10))

# main diagonal value 5
np.fill_diagonal(matrix, 5)

# under main diagonal value 1
np.fill_diagonal(matrix[1:, :], 1)

np.fill_diagonal(matrix[:, 1:], 4)

print(matrix)
