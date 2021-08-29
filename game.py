import turtle
from turtle import *
from random import randint

penup()
goto(-270,270)
write("TURTLE RACE", font=("Arial", 30, "bold"))
speed(500)
penup()
goto(-200,200)
x=-250
y=200
for r in range(5):
    speed(1000)
    pendown()
    forward(400)
    circle(x,180)
    forward(400)
    circle(x,180)
    
    x+=50
    y-=50
    penup()
    goto(-200,y)
goto(-200,-100)    
right(90)
pendown()
forward(200)
turtle.hideturtle()

    
a=Turtle()
a.color("red")
a.shape("turtle")
a.penup()
a.goto(-200,175)
a.pendown()


b=Turtle()
b.color("blue")
b.shape("turtle")
b.penup()
b.goto(-200,125)
b.pendown()

c=Turtle()
c.color("green")
c.shape("turtle")
c.penup()
c.goto(-200,75)
c.pendown()

d=Turtle()
d.color("yellow")
d.shape("turtle")
d.penup()
d.goto(-200,25)
d.pendown()

for r in range(133):
    a.forward(randint(1,5))
    b.forward(randint(1,5))
    c.forward(randint(1,5))
    d.forward(randint(1,5))




for t in range(180):
    a.forward(randint(3,5))
    a.right(1.001)
    b.forward(randint(2,4))
    b.right(1.0001)
    c.forward(randint(1,3))
    c.right(1.007)
    d.forward(randint(1,2))
    d.right(1.009)


for f in range(136):
    a.forward(randint(1,5))
    b.forward(randint(1,5))
    c.forward(randint(1,5))
    d.forward(randint(1,5))







