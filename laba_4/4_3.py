import math


def f1(x, a):
    if x == 0:
        return float('inf')  # обработка деления на ноль
    return 1 / (4 * (a**2) * (x**2)) + 1 / ((2 * a**4) * x) + 1 / (2 * a**6) * math.log(((-4)**2) / x)


def f2(x, a):
    arg = math.sin(a * x) + math.cos(a * x)
    if arg <= 0:
        return float('inf')  # обработка логарифма от неположительного числа
    return x / 2 + (1 / (2 * a)) * math.log(arg)


def main():
    a = 2
    start_x = math.pi
    end_x = 4 * math.pi
    step_size = 0.05 * math.pi

    x_values = [start_x + i * step_size for i in range(int((end_x - start_x) / step_size) + 1)]

    result_sum = sum(f1(x, a) + f2(x, a) for x in x_values)

    print("Сумма F1 + F2 для заданного диапазона x:", result_sum)


if __name__ == "__main__":
    main()
