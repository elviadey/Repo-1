import turtle
t = turtle.Turtle()

turtle.tracer(0,0)
turtle.bgcolor("light blue")  #setting background color
t.pensize(2)
t.penup()
t.goto(200,-85)               #going to starting position
t.pendown()
#==============================================================
def snowman():                #function to draw snowman
	
	t.fillcolor("white")
	t.begin_fill()			  #filling color in the body
	
	t.right(40)         	
	t.circle(-100,282)

	t.left(90)
	t.circle(-90,86)

	t.left(90)
	t.circle(-80,268)

	t.left(90)
	t.circle(-90,87)

	t.end_fill()

	t.pencolor("black")		#drawing eyes
	t.penup()
	t.goto(122,110)
	t.dot(15)
	t.goto(172,110)
	t.dot(15)

	t.goto(165,80)		   #drawing smile
	t.pendown()
	t.pencolor("red")
	t.left(45)
	t.circle(-20,180)
	t.right(90)
	t.forward(40)
	t.left(90)

	t.penup()			  #drawing nose
	t.goto(147,95)
	t.pendown()
	t.pencolor("orange")
	t.dot(10)	
	
	t.penup()			 #drawing hands
	t.goto(80,-20)
	t.pendown()
	t.pencolor("brown")
	t.left(50)
	t.pensize(2)
	t.forward(90)
	t.right(180)
	t.forward(20)
	t.right(250)
	t.forward(20)
	t.right(180)
	t.forward(20)
	t.right(70)
	t.forward(20)
	t.penup()
	t.goto(195,-20)
	t.pendown()
	t.right(140)
	t.forward(90)
	t.right(180)
	t.forward(20)
	t.right(250)
	t.forward(20)
	t.right(180)
	t.forward(20)
	t.right(70)
	t.forward(20)
#==============================================================
def drawPolygon(t, sides, size):
	# we need to return a list of vertices
	vertices = []

	angle = 360.0/sides  
	for i in range(sides):
		vertices.append(  t.pos()  )
		t.forward(size)
		t.right(angle)
	# loop ends

	return vertices

def drawEpicycloid(T, multiplier,sideSize,numVertices):
	t.pensize(0.0005)
	t.penup()
	t.goto(-300,225)							#going to starting position of epicycloid
	t.pendown()
	t.pencolor("yellow")
	v = drawPolygon(T, numVertices, sideSize)

	#==========================

	used = [False]*numVertices

	#do this for all values of current from 1 to 199
	for current in range(1, numVertices):
		T.penup()
		T.setposition( v[current] )
		T.pendown()

		while used[current] == False:

			used[current] = True # marking this place as used

			nextVertex = (current * multiplier) % numVertices

			# draws a line from current position to v[nextVertex]
			T.setposition( v[nextVertex] )

			current = nextVertex
#==============================================================
def flower():				#function to draw a flower
    
	t.penup()
	t.goto(2,107)
	t.pendown()
	t.pensize(2)
	t.pencolor("violet")
	
	for i in range(20):		#drawing petals 20 times for effect
		t.circle(40-i, 90)
		t.left(90)
		t.circle(40 - i, 90)
		t.left(18)

	t.pencolor("green")     #drawing the stem of the flower
	t.pensize(2.5)
	t.right(158)
	t.forward(90)

#==============================================================
def text() :                      #function to write text
	t.pencolor("black")
	t.penup()
	t.goto(-300,-60)
	t.pendown()
	t.write("Hi everyone! I'm Olaf, and I like warm hugs")
#==============================================================
#calling all functions
snowman()
drawEpicycloid(t,41,3,200)
flower()
text()
t.hideturtle()
turtle.done()
#==============================================================