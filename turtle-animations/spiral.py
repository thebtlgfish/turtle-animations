import turtle
import time
from colors import blk, rd, dkrd

turtle.bgcolor(blk)
t = turtle.Turtle()
colors = [rd,dkrd]
t.speed(100)

def animation():
    for number in range(600):
        t.forward(number+10)
        t.right(89)
        t.pencolor(colors[number%2])

time.sleep(15)
animation()
turtle.done()
