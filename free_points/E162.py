def hex():
    result = sum((15 * 16 ** (n - 1) - 43 * 15 ** (n - 1) + 41 * 14 ** (n - 1) - 13 ** n)
                 for n in range(1, 17))
    return f"{result:X}"


print(hex())
