with open("24.txt") as file:
    d = file.readline()

for i in "QRW":
    d = d.replace(i, "Q")
for i in "124":
    d = d.replace(i, "1")

r = 0
for s in range(len(d)):
    for e in range(s+r, len(d)):
        line = d[s:e+1]
        if "11" in line or "QQ" in line:
            break
        r = len(line)
print(r)
