from turtle import *


screensize(10000, 10000)
r = 20
lt(90)
tracer(0)

x = 20


for i in range(4):
    fd(x*r)
    rt(90)
    fd(x*r)
    lt(90)
    fd(x*r)
    rt(90)


update()
done()
