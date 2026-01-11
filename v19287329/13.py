import ipaddress

c = 0
for i in range(0, 33):
    net = ipaddress.ip_network(f"93.138.164.49/{i}", 0)
    if "93.138.160.0" in str(net):
        c += 1
print(c)

