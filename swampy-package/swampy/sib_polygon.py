# Polygon excercise from Week 0

# Name: Ethan Puzarne

from math import pi
from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

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

# 2-1,2
def square(turt, length):
	for i in range(4):
		fdrt(turt, length)

# Test
#square(bob, 20)

# 2-3
def polygon(turt, length, sides):
	angle_calc = 360/sides
	for i in range(sides):
		fdrt(turt, length, angle_calc)

# Test
#polygon(bob, 20, 10)

#  # 3-1
# def circle(turt, radius):
# 	circ = circumf(radius)
# 	sides = 45 # anything more takes too long
# 	length = circ/sides
# 	polygon(turt,length, sides)

# # Test
# #circle(bob, 100)

##  Helper functions 
def circumf(radius):
	return 2*pi*radius

def side_scale (theta):
 	# full circle broken into 45 pieces
 	max_sides = 45  # anything more takes too long
 	# get fraction of circle
 	fraction = theta/360.0
 	# scale number of sides down
 	return int(max_sides*fraction)

# # this is not perfect, the rounding error causes the 
# # final side to not be drawn unless the fraction is whole
# def arc(turt, radius, theta):
# 	sides = side_scale(theta)
#  	# get circumference of circle
#  	circ = circumf(radius)
#  	# get arc_length
#  	arc_length = circ * theta/360.0
#  	# get args for fdrt
#  	length = arc_length/sides
#  	angle_calc = theta/sides

#  	for i in range(sides):
#  		fdrt(turt, length, angle_calc)

# # Test
# arc(bob, 100, 360)


#####  Code refactor:
def polyline(turt, length, sides, angle):
	for i in range(sides):
		fdrt(turt, length, angle)

def polygon(turt, length, sides):
	angle_calc = 360/sides
	polyline(turt, length, sides, angle_calc)

# TEST 
#polygon(bob, 10, 20)

def arc(turt, radius, theta):
	# get circumference of circle
	circ = circumf(radius)
	sides = int(circ / 3 * theta / 360.0) + 1
	# get arc_length
	arc_length = circ * theta / 360.0
	# get args for polyline
	length = arc_length/sides
	angle_calc = theta/sides

	polyline(turt, length, sides, angle_calc)

#arc(bob, 30, 180)

def circle(turt, radius):
	circ = circumf(radius)
	sides = 45 # anything more takes too long
	length = circ/sides
	polyline(turt, length, sides, 360.0 / sides)

#circle(bob, 30)


wait_for_user()					
