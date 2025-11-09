with open("17.txt") as file:
    data = file.readlines()
    r = []
    for i in range(1, len(data)):
        a = int(data[i -1])
        b = int(data[i])
        if a % 3 == 0 or b % 3 == 0:
            r.append((a, b))
print(len(r))
print(sum(max(r, key=sum)))
