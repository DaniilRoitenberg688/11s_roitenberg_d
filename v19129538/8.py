import itertools

al = "0123456789ABCDEF"
r = 0
for i in itertools.product(al, repeat=8):
    if i.count("0") != 2:
        continue
    if len(set(i) & set("ABCDEF")) > 4:
        continue
    r += 1
print(r)
