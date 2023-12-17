import math


def area_with_base_and_height(b, h):
    return b * h / 2


def area_with_base_and_side(b, a):
    return (b / 4) * math.sqrt(4 * a ** 2 - b ** 2)


print("Площадь  через основание b и высоту h:")
print("S =", area_with_base_and_height(2, 2))

print("\nПлощадь через основание b и боковую сторону a:")
print("S =", area_with_base_and_side(2, 2))
