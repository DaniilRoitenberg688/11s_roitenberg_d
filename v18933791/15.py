from itertools import product


r = 0
for i in range(1, 21):
    for k in product("12", repeat=i):
        s = 1
        wf = False
        for j in k:
            if j == "1":
                s += 1
            if j == "2":
                s *= 2
            if s == 5:
                wf = True
        if s != 60 or wf:
            continue
        r += 1

print(r)


