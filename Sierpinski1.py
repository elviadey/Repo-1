import turtle
import random

#==================================================
# Functions
#==================================================

# find the point halfway between P and Q
def findHalfway( P, Q ):
	x = (P[0] + Q[0])/2
	y = (P[1] + Q[1])/2
	return (x,y)


#==================================================
# basic setup
#==================================================

T = turtle.Turtle()
T.hideturtle()
turtle.tracer(0,0) # no animation
T.penup()
T.setposition(-250, 200)

#==================================================
# Actual Code
#==================================================

# Draw a triangle and memorize the vertex coordinates
# I'm already at x=0 and y=0
v = []
for i in range(3):
	v.append( T.pos() )
	T.dot(10) # no real need for this, tbh
	T.forward(500)
	T.right(120)


#==================================================

for i in range(7000): # Do the following many times:

	# Pick a random vertex (out of v[0], v[1], v[2])
	choice = random.randint(0, 2) # chooses 0, 1, or 2

	# Move halfway to that vertex (from wherever you are)
	halfwayXY = findHalfway( T.pos() , v[choice] )
	T.setposition(halfwayXY)

	# Put a dot at that point
	T.dot(3)


#==================================================
# Finishing up
#==================================================

turtle.update() # need to do this if tracer(0,0)
turtle.done() # so it doesn't disappear after rendering
