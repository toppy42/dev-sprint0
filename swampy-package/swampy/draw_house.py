from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

world.clear()

def fdlt(turtle, length=0, angle=90):
  turtle.fd(length)
  turtle.lt(angle)

def fdrt(turtle, length=0, angle=90):
  turtle.fd(length)
  turtle.rt(angle)

def shift(turtle, distance=10):
  turtle.pu()
  turtle.fd(distance)
  turtle.pd()

def draw_house(turtle, size=10):
  fdlt(turtle, 3*size) # right 3
  fdrt(turtle, 2*size) # up 2
  fdrt(turtle, 1*size) # right 1
  fdlt(turtle, 2*size) # down 2
  turtle.bk(1*size)    # reverse left 1
  fdlt(turtle, 4*size) # right 4
  fdlt(turtle, 4*size, 45) # up 4
  fdlt(turtle, 5*size)     # left/up 5
  fdlt(turtle, 5*size, 45) # left/down 5
  fdlt(turtle, 4*size)     # down 4
  turtle.lt()              # rotate to up
  fdrt(turtle, 4*size)     # up 4
  fdrt(turtle, 7*size)     # right 7
  fdlt(turtle, 4*size)     # down 4

draw_house(bob)
shift(bob)
draw_house(bob)

wait_for_user()