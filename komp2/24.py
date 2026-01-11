with open("24.txt") as f:
    d = f.readline()


r = 0
for b in range(len(d)):
    for e in range(b + r, len(d)):
        k = d[b : e + 1]
        if len(k) < 3:
            continue
        f = k[0]
        s = k[-1]

        if not f.isdigit():
            break
        if len(set(k)) > 3:
            break
        if not s.isdigit():
            continue
        if int(s) % 2 != 0 or int(f) % 2 != 0:
            break
        if set(k) - set("1234567890") == set():
            continue
        if f == s:
            r = max(r, len(k) - k.count(f))
        else:
            r = max(r, len(k) - k.count(f) - k.count(s))
print(r)
