from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return (3*n + 5) * f(n-1)

for i in range(2074):
    f(i)

print(f(2073) / f(2070))


