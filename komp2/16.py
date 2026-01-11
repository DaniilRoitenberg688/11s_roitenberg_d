from functools import lru_cache

@lru_cache
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (n + 1) * f(n-1)

for i in range(1, 5038):
    f(i )

print(f(5037) / f(5034))
