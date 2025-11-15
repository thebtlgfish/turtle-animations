import turtle
import time
from colors import rd

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor(rd)
t.speed(3)
t.pensize(5)

def animation():
	angle = 1
	pos = t.pos()
	for i in range (45): # Right Side Of Mustache
		t.forward(20)
		angle += 1
		t.left(angle)
	
	t.pu()
	t.goto(pos)
	t.pd()
	t.left(180)
	angle2 = 1
	for i in range (45): #Left Side Of Mustache
		t.forward(20)
		angle2 += 1
		t.right(angle2)


time.sleep(10)
animation()
turtle.done()
