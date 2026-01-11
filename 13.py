# from ipaddress import *
# 
# for mask in range(15, 33):
#     net = ip_network(f"121.96.174.205/{mask}", 0)
#     c = 0
#     for ip in net:
#         if bin(int(ip)).count("1") == 12:
#             c += 1
#     if c == 10:
#         print(mask)
# 


from ipaddress import *

for mask in range(25, 33):
    net = ip_network(f"172.16.168.0/{mask}", 0)
    c = 0
    for ip in net:
        if bin(int(ip)).count("0") % 7 == 0:
            c += 1
    if c == 35:
        print(mask)
    

print(int("10000000", 2))
