from itertools import product

s = "алгоритм"
s = sorted(s)

res = 0
count = 0
for x in product(s, repeat=5):
    count += 1
    x_s = "".join(x)
    if x_s[0] != "г" and x_s.count("и") >= 2 and count % 2 == 1:
        res += 1

print(res)
    

