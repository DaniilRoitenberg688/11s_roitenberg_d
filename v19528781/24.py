import itertools
with open("24.txt") as f:
    d = f.readline()

for i in itertools.permutations("ABC"):
    d = d.replace("ABC", "0")
d = d.split("0")
print(d[0])
d = list(filter(lambda x: x != "", d))
print(len(max(d, key=len)))
