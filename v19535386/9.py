with open("9.txt") as f:
    d = f.readlines()

c = 0

for i in d:
    i = sorted(list(map(int, i.strip().split())))
    if len(set(i)) != len(i):
        continue
    ma = i[-1]
    mi = i[0]
    j = i[1:len(i)-1]
    if 2 * (ma + mi) > sum(j):
        continue
    c += 1

print(c)
