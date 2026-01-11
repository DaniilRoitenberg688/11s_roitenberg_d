from string import printable

p = printable[:64]

def f(n, k):
    r = ""
    while n > 0:
        r = p[n % k] + r
        n //= k
    return r


n = 6 * 512 ** 180 + 7 * 64 ** 181 + 3 * 8 ** 184 + 5 * 8 ** 125 - 65
print(f(n, 64).count("0"))
