for i in range(1000, 9999 + 1):
    f = int(str(i)[0]) + int(str(i)[1])
    s = int(str(i)[2]) + int(str(i)[3])
    t = int(str(i)[1]) + int(str(i)[2])
    l = [f, s, t]
    l.pop(l.index(min(l)))
    if "".join(map(str, sorted(l))) == "613":
        print(i)
    
