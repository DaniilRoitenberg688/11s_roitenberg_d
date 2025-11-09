from itertools import product


f = "yx320"
s = "1x3y3"

r = 10000000000

for i in product("0123456", repeat=2):
    f1 = f.replace("y", i[0]).replace("x", i[1])
    s1 = s.replace("y", i[0]).replace("x", i[1])
    sm = int(f1, 7) + int(s1, 9)
    if sm % 181 == 0 and r > sm:
        r = sm

print(r / 181)
