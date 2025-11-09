from itertools import product

ip = [bin(98), bin(162), bin(201), bin(94)]
uz = [bin(98), bin(162), bin(192), bin(0)]

ip = list(bin(201)[2:])
uz = list(bin(192)[2:])
print(ip)
print(uz)

r = 0

for v in product("10", repeat=8):
    l = []
    for i in range(8):
        l.append((bool(int(ip[i])) and bool(int(v[i]))) == bool(int(uz[i])))
    if all(l):
        r += 1
print(r)
