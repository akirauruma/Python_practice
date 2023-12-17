def smallest_natural_digit():
    x = 1
    while True:
        if all(set(str(x)) == set(str(x * i)) for i in range(2, 7)):
            return x
        x += 1


result = smallest_natural_digit()
print(result)
