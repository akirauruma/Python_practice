def revers(limit):
    total = 0
    for n in range(2, limit + 1):
        if n % 2 == 0:
            total += 20 * 30**(n // 2 - 1)
        elif n % 4 == 3:
            total += 100 * 500**(n // 4)
    return total


a = 9
result = revers(a)
print(result)
