def palindrome(s):
    return s == s[::-1]


def decimal(n):
    return bin(n)[2:]


decimal_sum = 0

for number in range(1, 1000000):
    decimal_str = str(number)
    binary_str = decimal(number)

    if palindrome(decimal_str) and palindrome(binary_str):
        decimal_sum += number

print(decimal_sum)
