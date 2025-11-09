from itertools import product
r = []
for n in range(4):
    for i in product("0123456789", repeat=n):
        for j in "0123456789":
            p = f"1{''.join(i)}4302{j}1"
            if int(p) % 3147 == 0:
                r.append(p)
print(*r, sep='\n')

n = 0
r = []
while n <= 10**10:
    l = str(n)
    if len(l) >= 8:
        if l[0] == '1' and l[-1] == '1' and l[-3:-7:-1] == "2034":
            r.append(l)
    n += 3147

print()
print(*r, sep='\n')
