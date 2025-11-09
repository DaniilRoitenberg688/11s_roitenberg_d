with open("17.txt", "r") as file:
    d = file.readlines()
    a = []
    for i in d:
        for j in d:
            i = i.strip('\n')
            j = j.strip('\n')
            if (int(j) + int(i)) % 120 == 0:
                a.append(int(j) + int(i))

print(len(a))
print(max(a))
