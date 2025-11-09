for i in range(2, 10**6):
    b = bin(i)[2:]
    k = b[:len(b) - 1]
    if i % 2 == 0:
        k = k + "01"
    else:
        k = k + "10"

#    if int(k, 2) == 2018:
    print(i)



