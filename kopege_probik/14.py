a = 17 * 16**455 + 2**67 - 4**47 + 58

a = oct(a)[2:]

print(a)
r = 0
for i in a:
    if int(i) % 2 == 0 and i != "6":
        r += 1
print(r)
