from ipaddress import *

a = ip_address("93.138.96.47")
for i in range(16, 32):
    n = ip_network(f"93.138.64.0/{i}", 0)
    if a in n:
        print(i)
    
                   
