with open("9.txt") as f:
    d = f.readlines()


n = 0

def F(m):
    if m[3]-m[2] == m[2]-m[1] and m[2]-m[1] == m[1]-m[0]:
        return 1
    else: return 0

for i in d:
    i = list(map(int, i.strip().split()))
    
    m = max(i)
    if m ** 2 <= (i[0] * i[1] * i[2] * i[3]) / m:
        continue
    i = sorted(i)
    if F(i):
        continue
    n += 1

print(n)
