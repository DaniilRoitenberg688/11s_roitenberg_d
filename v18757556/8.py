from itertools import product


l = "авлор"
l = sorted(l)
count = 0

for i in product(l, repeat=4):
    count += 1
    if i[0] == "л":
        break

print(count)
