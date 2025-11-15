import turtle
import time
from colors import lb

t = turtle.Turtle()
s = turtle.Screen()
t.speed(4)
t.pensize(3)
s.bgcolor(lb)

def animation():
	for i in range(30): # The Circle
		t.forward(30)
		t.left(15)
	Xpos, Ypos = t.pos()
	t.pu()
	changeX = 80
	x2 = Xpos - changeX
	t.setx(x2)
	t.pd()
	Xposition, Yposition = t.pos()
	t.forward(80)
	t.backward(80)
	x3 = Xposition - changeX
	t.pu()
	t.setx(x3)
	t.pd()
	t.forward(80)
	# The Mouth
	t.backward(80)
	t.pu()
	CPosX, CPosY = t.pos()
	changeXPos = 45
	t.setx(CPosX - changeXPos)
	t.left(180)
	t.pd()
	for i in range (27):
		t.forward(10)
		t.left(6.75)



time.sleep(15)
animation()
turtle.done()
