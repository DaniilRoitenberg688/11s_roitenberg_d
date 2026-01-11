r = 0
for i in range(345508 * 2026, 10**10, 2026):
    s = str(i)
    if s[0] != "7" or s[2:4] != "23" or s[5:7] != "64" or s[-1] != "8":
        continue
    if int(s[1]) % 2 != 0:
        continue
    if int(s[4]) % 2 != 0:
        continue
    print(i)
