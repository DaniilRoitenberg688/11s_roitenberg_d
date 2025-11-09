a1 = [
    [0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0],
]

# а б в г д е ж и к
a2 = [
    [0, 1, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 0],
]

current_postions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def swap_rows(matrix: list[list[int]], first: int, second: int) -> list[list[int]]:
    res = []
    f = []
    for i in range(len(matrix)):
        line = []
        for j in range(len(matrix[i])):
            if j == first:
                line.append(matrix[i][second])
                continue
            if j == second:
                line.append(matrix[i][first])
                continue
            line.append(matrix[i][j])
        if i == first:
            f = line
            continue
        if i == second:
            res.insert(first, line)
            res.append(f)
            continue
        res.append(line)
    return res

left_indexes = list(range(len(a2)))
new = a2.copy()
for i in range(len(a1)):
    one_count = a1[i].count(1)
    k = 0
    for j in range(len(a2)):
        if j in left_indexes and a2[i].count(1) == one_count:
            left_indexes.remove(j)
            k = j
            new = swap_rows(new, k, left_indexes[0])
            break

__import__('pprint').pprint(a1)
print()
__import__('pprint').pprint(new)




