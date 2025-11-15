q_str = 0
with open("9.txt", "r") as f:
    for st in f.readlines():
        sum3 = 0
        sumrep = 0
        d = {}
        row = [int(x) for x in st.split()]
        for x in row:
            d[x] = d.get(x, 0) + 1
        if len(d.keys()) == 4:
            for k, v in d.items():
                if v == 3:
                    sumrep = 3 * k
                else:
                    sum3 += k
            if sumrep ** 2 > sum3 ** 2:
                q_str += 1

print(q_str)
