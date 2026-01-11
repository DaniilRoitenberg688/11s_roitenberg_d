def s(n):
    r = ""
    while n > 0:
        r = str(n % 7) + r
        n //= 7
    return r


print(str(s(6 * 343 ** 5 + 5 * 49 ** 7 - 50)).count("6"))
