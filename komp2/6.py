from turtle import *

tracer(0)
left(90)
screensize(10000, 10000)
r = 20

for i in range(4):
    fd(3*r); lt(270); fd(5*r); rt(90)

lt(270)

for i in range(3):
    fd(5*r); rt(90); fd(3*r); lt(270); 

up()


for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*r, y*r)
        dot(3, "red")

update()
done()
    
