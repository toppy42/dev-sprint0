# Hello excercise from Week 0

# Name: Ethan Puzarne


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

# This is where you put code to move bob
# Make bob say "HELLO"

def fdlt(turtle, length=0, angle=90):
  turtle.fd(length)
  turtle.lt(angle)

def fdrt(turtle, length=0, angle=90):
  turtle.fd(length)
  turtle.rt(angle)

def shift_Right(t, x):
	t.pu()
	t.fd(x)
	t.pd()

def shift_Left(t, x):
	t.pu()
	t.lt(180)
	fdlt(t,x,180)
	t.pd()

# up 2, down 1, right 1, up 1, down 2
def draw_H(t, size):
	t.lt()
	t.fd(2*size)
	t.bk(1*size)
	t.rt()
	fdlt(t, 1*size)
	fdlt(t, 1*size, 180)
	fdlt(t, 2*size)

# up 2, right 1, left 1, down 1, right 1, left 1, down 1, right 1
def draw_E(t, size):
	t.lt()
	fdrt(t, 2*size)
	t.fd(1*size)
	t.bk(1*size)
	t.rt()
	fdlt(t,1*size)
	fdlt(t,1*size,180)
	fdlt(t,1*size)
	fdlt(t,1*size)
	t.fd(1*size)


# up 2, down 2, right 1
def draw_L(t, size):
	t.lt()
	fdlt(t,2*size,180)
	fdlt(t,2*size)
	t.fd(1*size)


# up 2, right 1, down 2, left 1, right 1
def draw_O(t, size):
	t.lt()
	fdrt(t,size*2)
	fdrt(t,size)
	fdrt(t,size*2)
	fdrt(t,size,180)
	t.fd(size)


def draw_HELLO(t, size=20):
	shift_Left(t,60)
	draw_H(t, size)
	shift_Right(t, size)
	draw_E(t, size)
	shift_Right(t, size)
	draw_L(t, size)
	shift_Right(t, size)
	draw_L(t, size)
	shift_Right(t, size)
	draw_O(t, size)


draw_HELLO(bob)

wait_for_user()					
