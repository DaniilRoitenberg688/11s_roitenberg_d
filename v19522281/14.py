import itertools

v = []
for x,y in itertools.product("01234567", repeat=2):
    f = f"{x}01{y}4"
    s = f"{x}{y}544"
    r = int(f, 9) + int(s, 8)
    if r % 89 == 0:
        v.append(r//89)
print(sorted(v))

