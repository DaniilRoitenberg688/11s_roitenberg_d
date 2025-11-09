r = []
for i in range(2422000, 2422080):
    d = set()
    for j in range(2, i // 2):
        if i % j == 0:
            d.add(j)
    if not d:
        r.append(i)

for i in enumerate(r):
    print(i[0] + 1, i[1])


