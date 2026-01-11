from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 0:
        return 0

    if n > 0 and n % 4 < 2:
        return f(n // 4) + n % 4

    if n % 4 >= 2:
        return f(n // 4) + n % 4 - 1
        
        
for i in range(10**9):
    a = f(i)
    b = f(i+1)
    if a == 27 and b == 20:
        print(i)
        break
