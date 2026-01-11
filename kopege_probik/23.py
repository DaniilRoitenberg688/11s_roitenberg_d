def f(n, k):
    if n == k:
        return 1
    if n > k:
        return 0
    return f(n +1, k) + f(n * 2, k)
    
    
print(f(1,12)*f(12,30))