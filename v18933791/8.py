from itertools import permutations, product


def alg(l: str):
    while "111" in l or "22" in l:
        l = l.replace("111", "2", 1)
        l = l.replace("222", "1", 1)
        l = l.replace("221", "1", 1)
        l = l.replace("122", "1", 1)
        l = l.replace("22", "2", 1)
    return l
    

r = 0
for i in range(20, 30):
    for j in product("12", repeat=i):
        j = alg(str(j))
        if j.count("2") == 9:
            r += 1
print(r)

