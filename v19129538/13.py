import itertools


r = 10 ** 8
for x, y  in itertools.product(range(8), repeat=2):
    f = f"{y}04{x}5"
    s = f"253{x}{y}"
    n = int(f, 11) + int(s, 8)
    if n % 117 == 0 and r > n:
        r = n
print(r // 117)
