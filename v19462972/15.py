def f(
    x,
):
    return not (
        (215 <= x <= 264)
        <= ((not (a1 <= x <= a2) and (221 <= x <= 294)) <= (not (215 <= x <= 264)))
    )


d = [y for x in (215, 221, 264, 294) for y in (x, x + 0.1, x - 0.1)]

r = []

for a1 in d:
    for a2 in d:
        k = [f(x) == 1 for x in d]
        if a1 <= a2 and all(f(x) == 1 for x in d):
            r.append(a2 - a1)
print(r)
print(min(r))
