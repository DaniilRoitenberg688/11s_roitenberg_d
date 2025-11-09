with open("28130_B.txt") as file:
    data = [int(i) for i in file.readlines()]
    c = 0
    for i in range(len(data) ):
        for j in range(i+1, len(data)):
            if (data[i] + data[j]) % 80 == 0 and (data[i] > 50 or data[j] > 50):
                c += 1
    print(c)
