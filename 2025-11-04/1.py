from itertools import *
from turtle import *
from time import *
from itertools import *
from math import *
from ipaddress import *
from math import *
from functools import *
def f1():


    # 2 72559

    t = "12,14,19,27,34,35,36,46,49,58,67,68,78"
    g = "AB,AD,BV,BD,VE,EI,EK,KI,ID,IJ,JD,JG,GA"
    t = t + ',' + t[::-1]
    g = g + ',' + g[::-1]

    s = "ABVGDEJIK"

    for ss in permutations(s):
        nt = g
        for i, v in enumerate(ss):
            nt = nt.replace(v, str(i + 1))
        if set(nt.split(',')) == set(t.split(',')):
            print(ss)


def f2():
    def f(x,y,z,w):
        return ((x and (not(y)))or (x==z) or (not(w)))

    for a1, a2, a3, a4 in product([0, 1], repeat=4):
        tab = [(a1, a2, 0, 0), (1, 1, 1, 0), (1, 0, a3, a4)]
        if len(tab) == len(set(tab)):
            for p in permutations('xyzw'):
                if [f(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
                    print(p)

def f4():

    def f(n):
        s=bin(n)[2:]
        if s.count('1')%2==1:
            s=s+'10'
        else:
            s=s+'00'
        return int(s,2)

    for n in range(1,100):
        if f(n)>123:
            print (f(n))
            break
def f5():


    screensize(5000, 5000)
    tracer(0)
    down()
    k = 20
    for i in range(2):
        fd(27 * k)
        rt(90)
        fd(8 * k)
        rt(90)
    up()

    fd(4 * k)
    rt(90)
    fd(2 * k)
    lt(90)
    down()

    for i in range(2):
        fd(17 * k)
        rt(90)
        fd(7 * k)
        rt(90)

    up()

    for i in range(-50, 50):
        for j in range(-50, 50):
            goto(i * k, j * k)
            dot(3, "Red")

    done()

def f6():
    old=640*480*16 #размер старой фото
    new=1280*960*24 #размер новой фото
    v_old=old*12/1  #скорость канала  бит в сек
    v_new=v_old*2  # скорость канала после увеличесния в два раза
    print (v_old/old) #кол-во старых фото на старой скорости в сек
    print (v_new/new) #кол-во новых фото на новой скорости в сек



def f7():

    s=list("АВТОР")
    s.sort()
    print(tuple("ТАРА"))

    print (s)
    # скажем enumerate начинать нумерацию с 1
    for i,v in enumerate(product(s,repeat=4),1):
        if v==tuple('ТАРА'):
            print (i,v)




def f8():
    ts=time()
    with open("8.txt") as f:
        a=[]
        cnt=0
        for s in f:
            s=list(map(int,s.split()))
            # print (s)
            a.append(s)
        # транспонируем массив
        ta=[list(row) for row in zip(*a)]
        # print (ta)

        for m in a:
            k=[]


            for i,v in enumerate(m):

                if m.count(v)==1:

                    if ta[i].count(v)>=335+1: #встречается в столбце не менее 335+1 раз
                        if v<sum(m)/len(m): #меньше среднеарифметического строки
                            k.append(v)
            if len(k)==1:
                cnt+=1
        print (cnt)
        print (time()-ts)


def f8_1():
    ts=time()
    with open("8.txt") as f:
        a=[]
        cnt=0
        for s in f:
            s=list(map(int,s.split()))
            a.append(s)

        # транспонируем массив
        ta=[list(row) for row in zip(*a)]

        # создаем словарь вхождений чисел
        td=[]
        for m in ta:
            di={k:m.count(k) for k in set(m)}
            td.append(di)

        # или в одну строчку
        # td=[{k:m.count(k) for k in set(m)} for m in ta]

        for m in a:
            k=[]


            for i,v in enumerate(m):

                if m.count(v)==1:

                    if td[i][v]>=335+1: #встречается в столбце словаря  не менее 335+1 раз
                        if v<sum(m)/len(m): #меньше среднеарифметического строки
                            k.append(v)
            if len(k)==1:
                cnt+=1
        print (cnt)
        print (time()-ts)
        # сравните время выполнение со словарем и без

def f10():
    csymb=(26+10)
    mbit=ceil(log2(csymb)) # кол-во бит на 1 символ
    print (ceil(mbit*13/8)) #байт на 1 код
    print (ceil((ceil(log2(60))+ceil(log2(12)))/8)) #байт на срок

def f11():
    def f(s):
        while '111' in s:
            s=s.replace('111','22',1)
            s = s.replace('222', '11', 1)

        return s.count('1')
    maxi=-1
    for n in range(100,1000):
        cnt=f('1'*n)
        if cnt>maxi:
            maxi=cnt
            print (n,maxi)


def f12():

    ipn=ip_network('208.32.128.64/255.255.192.0',0)
    print (ipn)


def f13():
    def f(s,n):
        s=s[::-1]
        k=0
        for i,v in enumerate(s):
            k+=int(v)*(n**i)
        return (k)

    for x in range(39):
        i=f("653071",39)+f("42037",39)+x*(39**2)+x*(39**2)
        if i%14==0:
            print (i//14)
            break

def f14():
    def f(x, a1, a2):
        P = 215 <= x <= 264
        Q = 221 <= x <= 294
        A = a1 <= x <= a2
        return (not(( P ) <= (( (not(A))and(Q)) <=( not(P)))))

    m = []
    d = []
    for x in (215, 264, 221, 294):
        d.append(x)
        d.append(x + 0.01)
        d.append(x - 0.01)

    for a1 in range(1, 300):
        for a2 in range(1, 300):
            if any((f(x, a1, a2) for x in d)) == False:
                # print (a2-a1)
                m.append(a2 - a1)

    print(min(m))
def f15():
    def f5z(n):
        return int(10000<=n<=99999)

    def f5d(n):
        return int((n%5==0))

    with open("15.txt") as f:
        a=[]
        maxi=-10**20
        max321=-1
        cnt=0
        for s in f:
            s=s.strip()
            a.append(int(s))
            if int(s)%1000==321:
                max321=max(max321,int(s))

        for a1,a2,a3 in zip(a,a[1:],a[2:]):
            if (a1+a2+a3)>max321:
                if (f5z(a1)+f5z(a2)+f5z(a3))==2 and (f5d(a1)+f5d(a2)+f5d(a3))>=1:
                    maxi=max(maxi,(a1+a2+a3))
                    cnt+=1
        print (cnt,maxi)

def f1719():
    def f(a, b, m):
        if a + b >= 41: return m % 2 == 0
        if m == 0: return 0
        h = [f(a + 1, b + 2, m - 1), f(a + 2, b + 1, m - 1), f(a * 2, b, m - 1), f(a, b * 2, m - 1)]

        # для 19 задачи если неудачный ход
        # return any(h) if (m +1) % 2 == 0 else any(h)

        # для 20-21 задачи и (19 задачи для любых ходов)
        return any(h) if (m + 1) % 2 == 0 else all(h)

    print("19:", [s for s in range(1, 32 + 1) if f(8, s, 2)])
    print("20:", [s for s in range(1, 32 + 1) if (not f(8, s, 1)) and f(8, s, 3)])
    print("21:", [s for s in range(1, 32 + 1) if (f(8, s, 2)) or f(8, s, 4)])

def f20():
    with open("20.txt") as f:
        s=f.readline()
        #
        k=set(list(s))
        k.remove('A')
        for c in k:
            s=s.replace(c,':')
        s=s.split(':')
        print (len(max(s)))

        # или
        # s=s.replace("B",":").replace("C",":")
        # s = s.split(':')
        # print(len(max(s)))

def f21():
    def f(N):
        a=[]
        for i in range(1,ceil(N**0.5)+1,1):
            if N%i==0 :
                if i%2==0:
                    a.append(i)
                if (N//i)%2==0:
                    a.append(N//i)
        a=list(set(a))
        a.sort()
        return a


    for i in range(95632,95700+1):
        a=f(i)
        if len(a)==6:
            print (a)


def f22():
    data = []

    def centa(clu):
        a = []
        for p1 in clu:
            suma = 0
            for p2 in clu:
                suma += dist(p1, p2)
            a.append([suma, p1])

        return min(a)[1]

    # with open("demo_2025_22_A.txt") as f:

    with open("demo_2025_22_B.txt") as f:
        for s in f:
            m = list(map(float, s.replace(',', '.').split()))
            # print (m)
            data.append(m)

    clusters = []
    while data:

        cl = [data.pop()]

        for p1 in cl:
            sosedi = [p2 for p2 in data if dist(p1, p2) < 1]
            for p2 in sosedi:
                if p2 in data:
                    data.remove(p2)
                cl.append(p2)
        clusters.append(cl)

    print([len(cl) for cl in clusters])

    px = 0
    py = 0

    for cl in clusters:
        px += centa(cl)[0]
        py += centa(cl)[1]

    px = px * 10_000 / len(clusters)
    py = py * 10_000 / len(clusters)

    print(px // 1, py // 1)

def f25():

    @lru_cache(None)
    def f(n):
        if n <= 2:
            return n - 1
        if n > 2:
            return 3 * f(n - 1) - f(n - 2)

    # заполняем кэш
    for i in range(1,7):
        f(i)

    print(f(6))

def f27():
    def f(x, y):
        if x == y:
            return 1
        if x > y:
            return 0
        return f(x + 2, y) + f(x * 3, y)

    print(f(1, 49))

f27()