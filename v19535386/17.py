from itertools import combinations
with open('17.txt', 'r') as file:
    s = list(map(int, file.read().split()))
count = max_sum = 0
pairs = combinations(s, 2)
for pair in pairs:
    if sum(pair) % 10 == 0:
        count += 1
        max_sum = max(max_sum, sum(pair))
print(count, max_sum)
