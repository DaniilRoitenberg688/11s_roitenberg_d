from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 5:
        return 4**4
    if n > 4:
        return 4 * f(n - 4) + 4
    return 1


for i in range(1, 4049):
    f(i)
    
print(f(4048)/f(4036))
