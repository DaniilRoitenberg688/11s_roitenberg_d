r = 10 ** 6 
for i in range(12):
    f = int(f"3{i}DA", 14)
    s = int(f"5{i}A6", 12)
    if (f + s) % 81 == 0:
        print((f + s) / 81)
