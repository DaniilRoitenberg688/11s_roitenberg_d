def Del(n,m):
    return n%m == 0

def f(x):
    return Del(70, A) and (Del(x,28) <= ((not Del(x, A)) <= (not Del(x, 21))))


for A in range(100, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(A)
