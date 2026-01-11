import itertools

res = 0
for i in "12345678":
    for v in itertools.product("012345678", repeat=4):
        s = i + "".join(v)
        if s.count("5") != 1:
            continue
        for k in "1379":
            s = s.replace(k, "1")
        if "51" in s or "15" in s:
            continue
        res += 1
print(res)