from ipaddress import *

res = 100000000

for i in range(1, 17):
    net = ip_network(f"114.91.57.39/{i}", 0)
    c = 0
    for a in net:
        if bin(int(a)).count("1") % 2 == 0:
            c += 1
    res = min(res, c) 

print(res)


