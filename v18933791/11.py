a = []

for i in range(1, 5):
    if i == 1:
        a.append(1)
    else:
        a.append(a[-1] * (2 * i + 1))
print(a[-1])

