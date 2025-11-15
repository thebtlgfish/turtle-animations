import turtle
import time
from colors import yw, lb

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor(lb)
s.setup(width=800, height=800)
t.speed(5)
t.pensize(3)
t.color(yw)

def animation():
    for i in range(40):
        t.forward(100)
        t.left(95)



time.sleep(10)
animation()
turtle.done()

