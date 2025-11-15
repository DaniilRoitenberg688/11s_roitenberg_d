# print("x y w z")
#
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (x <= (z <= w)) and (z <= (y == (not w)))
#                 if f == 0:
#                     print(x, y, w, z)
# #0 0 0 1
# #1 0 0 1
# #1 1 0 1
#
# #zxwy
#
#
#
#


print("x y w z")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = ((not z) == (not y)) or ((not x) and y) or w
                if f == 0:
                    print(x, y, w, z)
#zxwy


# print()
# print("x y w z")
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f2 = (x <= y) == (w and (not z))
#                 if f2 == 0:
#                     print(x, y, w, z)
#
