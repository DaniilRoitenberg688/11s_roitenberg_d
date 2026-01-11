from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 4000:
        return n
    if n >= 4000 and n % 7 == 0:
        return n + f(n//7)
    else:
        return 567 + f(n-3)

for i in range(-700000, 10**6):
    n = f(i)
    if n > 80000:
        print(i)
        break
