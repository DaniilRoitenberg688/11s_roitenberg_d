nc = "13579"
c = 0
for i in range(100_000, 999_999 + 1):
    h = hex(i)[2:]
    if "2" not in h:
        continue
    if h.count("2") > 1:
        continue
    n = h.index("2")
    if n == 0:
        if h[n + 1] not in nc:
            c += 1
            continue

    elif n == len(h) - 1:
        if h[n - 1] not in nc:
            c += 1
            continue

    else:
        if h[n + 1] not in nc and h[n - 1] not in nc:
            c += 1
            continue
print(c)
