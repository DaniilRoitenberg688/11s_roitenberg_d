n = 138

while True:
    l = "0" + "1" * n + "2" * n + "0"
    while "00" not in l:
        l = l.replace("02", "101", 1)
        l = l.replace("11", "2", 1)
        l = l.replace("12", "21", 1)
        l = l.replace("010", "00", 1)
    dels = set()
    for i in range(2, int(l) // 2):
        if int(l) % i == 0:
            dels.add(i)
    if not dels:
        print(l)
        print(n)
        break
    n += 1
