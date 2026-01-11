from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    return 2 * (g(n - 3) + 8)


@lru_cache(maxsize=None)
def g(n):
    if n < 10:
        return 2 * n
    return 1 + g(n - 2)


for i in range(15549):
    f(i)

print(f(15548))