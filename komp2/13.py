from ipaddress import *

net = ip_network("98.71.254.171/255.248.0.0", 0)
res = []
for i in net:
    if bin(int(i)).count("1") % 7 == 0:
        res.append(i)

print(min(res))
