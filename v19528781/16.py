from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return (f(n-1) - f(n-2)) * n

for i in range(1, 10):
    f(i)

print(f(8))
