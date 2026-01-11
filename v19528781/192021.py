def f(n, m):
    if n <= 19:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(n-1, m-1)]
    if n%3==0:
        h.append(f(n//3, m-1))
    else:
        h.append(f(n-2, m-1))

    if n%5==0:
        h.append(f(n//5, m-1))
    else:
        h.append(f(n-3, m-1))

    return any(h) if (m+1) % 2 ==0 else all(h)


print([i for i in range(20, 100) if not f(i, 1) and f(i, 2)])
print([i for i in range(20, 100) if not f(i, 1) and f(i, 3)])
print([i for i in range(20, 100) if not f(i, 2) and f(i, 4)])

