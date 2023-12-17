def is_palindrome(num):
    return str(num) == str(num)[::-1]


palindromes = []

for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        if is_palindrome(product):
            palindromes.append(product)

print("Полиндромы для трехразрядных чисел:")
print('\n'.join(map(str, palindromes)))