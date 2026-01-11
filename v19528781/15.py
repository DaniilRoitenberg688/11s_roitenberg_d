def f(x):
    Q = 4 <= x <= 51
    P = 19 <= x <= 84
    A = a1 <= x <= a2
    h = (not P) <= (not(Q and (not A)))
    return Q <= h

d = []
for i in (4, 19, 51, 84):
    d.extend([i-0.1, i, i+0.1])

for a1 in d:
    for a2 in d:
        if a1 < a2 and all(f(x) for x in d):
            print(a2 - a1)

