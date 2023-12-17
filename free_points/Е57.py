def count_fractions_with_more_digits(n):
    numerator, denominator, count = 1, 1, 0
    for _ in range(n):
        numerator, denominator = 2 * denominator + numerator, denominator + numerator
        count += len(str(numerator)) > len(str(denominator))
    return count


result = count_fractions_with_more_digits(1000)
print(result)
