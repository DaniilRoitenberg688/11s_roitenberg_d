from fnmatch import fnmatch
for i in range(0 , 10**9, 3123):
    l = str(i)
    if fnmatch(l, "12*63?5?"):
        print(l)
