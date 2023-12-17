import numpy as np

matrix = np.array([0, 0, 1, 5, 0, 1])

zero_indices = np.where(matrix == 0)

print("Индексы нулевых элементов:", zero_indices)
