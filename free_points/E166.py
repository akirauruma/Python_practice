from itertools import product

def compute():
    ans = 0
    digits = range(10)
    for combo in product(digits, repeat=10):
        b, c, d, e, i, k, a, g = combo[:8]
        m = b + c + d - e - i
        f = b + c + d * 2 - e - i - k
        o = a + b + d - g - k
        j = a + b + c - g - m
        l = a + b + c + d - i - j - k
        h = a + b + c + d - e - f - g
        n = a + c + d - f - j
        p = a + b + c - h - l
        if all(0 <= x <= 9 for x in [m, f, o, j, l, h, n, p]):
            ans += 1
    return str(ans)


if __name__ == "__main__":
    print(compute())
