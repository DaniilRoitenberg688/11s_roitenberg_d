# def f(a, n):
#     if a < 10: return n % 2 == 0
#     if n == 0: return 0
#     h = []
#     for i in range(1, 6):
#         h.append(f(a-i, n-1))
#     if a % 2 == 0:
#         h.append(f(a//2, n-1))
#
#     return any(h) if (n-1)%2==0 else all(h)
#
#
# print([i for i in range(10, 100) if f(i, 2)])
# print([i for i in range(10, 200) if not f(i, 1) and f(i, 3)])
# print([i for i in range(10, 100) if not f(i, 2) and f(i, 4)])


def f(a, b, n):
    if b <= a: return n % 2 == 0
    if n == 0: return 0
    h = [f(a + 2, b, n - 1), f(a * 3, b, n-1)]
    return any(h) if (n+1) % 2 == 0 else all(h)

print([i for i in range(16, 100) if f(15, i, 2)])
print([i for i in range(16, 200) if not f(10, i, 1) and f(10, i, 3)])
print([i for i in range(16, 200) if not f(5, i, 2) and f(5, i, 4)])
