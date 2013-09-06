# Flower excercise (4.2) from Week 0

# Name: Ethan Puzarne


from TurtleWorld import * 
# when importing sib_polygon, must comment out world, bob, and wait_for_user
from sib_polygon import arc
from math import asin, pi, atan, cos
world = TurtleWorld()			
bob = Turtle()				


# This is where you put code to move bob

# convert from radians to degrees
def to_degrees(radians):
	'''Convert from radians to degrees'''
	return radians * 360.0 / (2*pi)

def get_radius(petal_length, petal_width):
	''' using length and width of petals, compute
	radius of arc that makes up half of a petal'''
	#debug print("petal_length and width: " + str(petal_length) + " " + str(petal_width))
	# compute angle of triangle made up by petal
	outer_tri_rads = atan(float(petal_width)/float(petal_length))
	# debug print("outer tri: " + str(outer_tri_rads))
	# compute angle of triangle made up by radius and half of petal length
	inner_tri_rads = (pi/2)-outer_tri_rads
	# debug print(inner_tri_rads)
	# compute radius
	radius = petal_length / 2 / cos(inner_tri_rads)
	return int(radius)

def petal(turt, petal_length, petal_width):
	'''Turtle draws petal with given length and width
	then ends in same position and orientation '''
	# get radius of arc
	radius = get_radius(petal_length, petal_width)
	# debug print(radius)
	# get arc in radians from triangle made up by radius and half petal length
	arc_rads = 2*asin(petal_length/2.0/radius)
	# convert to degrees
	arc_degrees = to_degrees(arc_rads)
	# draw arc, then turn and draw mirrored arc
	arc(turt, radius, arc_degrees)
	turt.rt(180-arc_degrees)
	arc(turt, radius, arc_degrees)
	turt.rt(180-arc_degrees)

def flower(turt, petals, petal_length, petal_width):
	''' flower() takes a turtle, number of petals, length and width of petals
	and draws the appropriate flower'''
	petal_angle = 360.0/petals
	for i in range(petals):
		# draw petal, then rotate to draw next petal
		petal(turt, petal_length, petal_width)
		turt.rt(petal_angle)

# increase speed so I don't die of old age
bob.delay = 0.01
#petal(bob, 50, 50)
#flower(bob, 10, 50, 50)
#flower(bob, 20, 50, 20)
flower(bob, 20, 100, 50)
wait_for_user()					

