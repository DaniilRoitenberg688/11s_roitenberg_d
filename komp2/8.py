# import itertools
# 
# 
# l = sorted("кодим")
# 
# r = 0
# 
# for i in itertools.product(l, repeat=5):
#     if i.count("м") != 2:
#         continue
#     if "мм" in "".join(i):
#         continue
#     r += 1
#     print(*i)
# 
# print(r)
# 

from itertools import *
 
k = 0
 
for x in product( sorted('ДИКМО'), repeat=5):
    s = ''.join(x)
    k += 1
    if s.count('М')==2 and 'ММ' not in s:
        print(k,s)
