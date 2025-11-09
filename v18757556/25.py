for i in range(210_235, 210_301):
    dels = set()
    for j in range(2, i//2 + 1):
        if i % j == 0:
            dels.add(j)
    if len(dels) == 4:
        print(*sorted(list(dels)))
        
