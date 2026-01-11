from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    return f(n//10) + (n % 10)

c = 0
for i in range(765_432_015, 1_542_613_239+1):
    if f(i+1) < f(i):
        c+=1
print(c)
        
        
