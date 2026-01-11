from turtle import *


screensize(10000, 10000)
tracer(0)




lt(90)
k= 60

for i in range(4):
    fd(12*k)
    rt(90)


rt(30)

for i in range(3):
    fd(k*8)
    rt(60)
    fd(8*k)
    rt(120)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(3, "red")

update()
done()
    

