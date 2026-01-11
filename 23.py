# def f(x, y):
#     if x == y:
#         return 1
#     if x < y:
#         return 0
#     return f(x-3, y) + f(x//3, y)

# print(f(80, 27) * f(27, 3))


# def f(n, m):
#     if n < m or n == 12 or n == 15:
#         return 0
#     if n == m:
#         return 1
#     h = [f(n - 1, m)]
#     if n % 3 == 0:
#         h.append(f(n / 3, m))
#     if n % 2 == 0:
#         h.append(f(n / 2, m))
#     return sum(h)


# #print(f(19, 1) - (f(19, 12) * f(12, 1) + f(19, 15) * f(15, 1)))
# print(f(19,1))
#
#
#
def f(n, m, c):
    if n == m:
        return 1
    if n > m + 1 or n < 0:
        return 0

    if c != "a":
        return f(n - 1, m, "a") + f(n + 3, m, "b") + f(n * 2, m, "c")
    else:
        return f(n + 3, m, "b") + f(n * 2, m, "c")


print(f(3, 12, ""))
