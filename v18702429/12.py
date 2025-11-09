l = 0
for i in range(3, 10000 + 1):
    line = "555" + "2" * i
    while "52" in line or "2222" in line or "1122" in line:
        if "52" in line:
            line = line.replace("52", "11", 1)
        if "2222" in line:
            line = line.replace("2222", "5", 1)
        if "1122" in line:
            line = line.replace("1122", "25", 1)
    s = sum(map(int, line))
    if s == 64:
        l = i
print(l)
