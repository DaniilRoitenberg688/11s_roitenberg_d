for i in range(1, 10**6 + 1):
    b = bin(i)[2:]
    k = int(f"1{b}1", 2)
    if i % 2 == 0:
        k = int(b + b[-2] + b[-1], 2)
        
    if k > 100:
        print(i)
        break
    
