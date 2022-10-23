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

# Just copy-pasted our old drawPolygon function
# draw a polygon using turtle t with n sides, with each being size long
# return the list of vertices
def drawPolygon(t, n, size):
	# we need to return a list of vertices
	vertices = [None]*n # vertices = []

	angle = 360/n # play around with this
	for i in range(n):
		vertices[i] = t.pos() # vertices.append(  t.pos()  )
		# we could do t.dot(10) or something here, but we won't bother
		t.forward(size)
		t.right(angle)
	# loop ends

	return vertices

#==================================================
# Main code
#==================================================
def main():

	#==================================================
	# Setup

	T = turtle.Turtle()
	T.hideturtle()
	turtle.tracer(0,0) # no animation
	T.penup()
	T.setposition(-250, 200)
	turtle.bgcolor("black")
	#==================================================
	# Actual code

	# Draw a triangle and memorize the vertex coordinates
	n    = 3  # number of vertices
	size = 500 # length of each side of my polygon
	c = ['orange','green','white'] # just adding some colour!
	v = drawPolygon(T, n, size)

	for i in range(24710): # Do the following many times:

		choice = random.randint(0, n-1) # Pick a random vertex (choice=0,1,or 2)

		# Move halfway to that vertex (from wherever you are)
		halfway = findHalfway( T.pos() , v[choice] )
		T.setposition(halfway)

		# Put a dot at that point
		T.pencolor( c[ choice % len(c) ] ) # think about what this does
		T.dot(2)


	#==================================================
	# Finishing up

	turtle.update() # need to do this if tracer(0,0)
	turtle.done() # so it doesn't disappear after rendering

main()