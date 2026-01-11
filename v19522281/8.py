import itertools

c = 0

for v in "0123456":
    for i in itertools.product("0123456",repeat=3):
        n = v + "".join(i)
        print(n)
        l = list(map(int, list(n)))
        if l[0] > l[1] > l[2] > l[3]:
            c += 1

print(c)

