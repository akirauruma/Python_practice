def find_largest_repeating_cycle(limit):
    max_cycle_length, result_d = 0, 0

    for d in range(2, limit):
        remainder, position, remainders = 1, 0, {}

        while remainder and remainder not in remainders:
            remainders[remainder], remainder, position = position, (remainder * 10) % d, position + 1

        max_cycle_length, result_d = (max(max_cycle_length, position - remainders.get(remainder, 0)),
                                      result_d if max_cycle_length >= position - remainders.get(remainder, 0) else d)

    return result_d


if __name__ == "__main__":
    result = find_largest_repeating_cycle(1000)
    print("значение d < 1000, где 1/d содержит самый длинный повторяющийся цикл в десятичной дробной части:", result)
