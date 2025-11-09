from itertools import product


for x, y in product("0123456789ABC", repeat=2):
    f = f"8{x}78{y}"
    s = f"79{x}{y}7"
    if (int(f, 13) + int(s, 18)) % 9 == 0:
        print((int(f, 13) + int(s, 18)) // 9)
        
