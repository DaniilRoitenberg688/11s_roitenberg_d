from itertools import permutations


data = [
    [False, True, True, True, True],
    [False, False, False, True, True],
    [True, True, False, False, True],
]

l = "yzwx"
for var in permutations(l):
    a = []
    for i in data:
        a.append(
            (
                (
                    not (i[var.index("y")] or i[var.index("z")])
                    or (i[var.index("z")] and i[var.index("w")])
                )
                is (
                    not (
                        not (i[var.index("x")] and i[var.index("z")])
                        or (i[var.index("w")] or i[var.index("y")])
                    )
                )
            )
            is bool(i[-1])
        )
    if all(a):
        print(var)
