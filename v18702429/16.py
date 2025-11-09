l = []
for i in range(1, 2025):
    if i < 11:
        l.append(i)
    else: 
        l.append(i + l[-1])

print(l[-1] - l[-4])
