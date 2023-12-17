from scipy.optimize import ridder
import numpy as np


def equation(x):
    return np.exp(x) - x**2


a = -100
b = 100

root = ridder(equation, a, b)

print("Корень уравнения:", root)
