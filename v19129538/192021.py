def fn(n,m):
    if n >= 54: return m%2==0
    if m == 0: return 0
    h = [fn(n+2, m-1), fn(n*2, m-1)]
    return any(h) if (m-1)%2==0 else all(h)

print([i for i in range(1, 54) if not fn(i,2) and fn(i, 4)])



# def fn(s,m):
#     if s >= 39: return m%2==0
#     if m == 0: return 0
#     h = [fn(s+1, m-1), fn(s+3,m-1), fn(s*2, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
#
# print(19, [i for i in range(1, 39) if fn(i,2)])
# print(20, [i for i in range(1, 39) if not fn(i,1) and fn(i, 3)])
# print(20, [i for i in range(1, 39) if not fn(i,2) and fn(i, 4)])

# def fn(a, b, m):
#     if a >= 479 or b >= 479: return m%2==0
#     if m == 0: return 0
#     h = [fn(a+1, b, m-1), fn(a+3, b, m-1), fn(a*2, b, m-1), fn(a, b+1, m-1), fn(a, b+3, m-1), fn(a, b*2, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)

# print(19, [s for s in range(1, 479) if fn(239, s, 2)])
# print(19, [s for s in range(1, 479) if not fn(239, s, 1) and fn(239, s, 3)])
# print(19, [s for s in range(1, 479) if not fn(239, s, 2) and fn(239, s, 4)])
