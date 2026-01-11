import itertools

r = 0
for i in itertools.product("слон", repeat=5):
    if i.count("с") == 1:
        r += 1
print(r)
    
