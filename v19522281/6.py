from turtle import *


def arc(rad, a, b, ang):
    circle(-rad*r, ang)


screensize(10000, 10000)
tracer(0)
lt(90)
r = 20 


rt(180)
fd(2*r)
rt(90)
fd(40*r)
rt(90)
fd(2*r)

for i in range(4):
    arc(5, 5, 0, 180)
    rt(180)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(r*x, r*y)
        dot(3, "red")



update()
done()



