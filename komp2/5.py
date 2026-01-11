f = set()

for i in range(20, 51):
    b = bin(i)[2:]
    b += str(sum(map(int, b)) % 2)
    b += str(sum(map(int, b)) % 2)
    s = int(b, 2)
    print(s)
    f.add(s)

print(len(f))

