#I have called all functions at the end (line 244)
#Each part of the problem is demarcated
import turtle  
import math   

t = turtle.Turtle()
#==========================================
#Problem 2-3(a)

#defining function
def drawSquare(x, y, side):
    #going to starting coordinates
    t.penup() 
    t.goto(x,y)
    t.pendown()

#running loop 4 times to draw square
    for i in range(4) :
        t.forward(side)
        t.right(90)


#==========================================
#Problem 2-3(b)  

#defining function
def drawTiltedSquare(x, y, side):
    #going to starting coordinates
    t.penup() 
    t.goto(x,y)
    t.pendown()
    #changing the orientation of the turtle to make the square tiled
    t.right(45)
    #running loop 4 times to draw tiled square
    for i in range(4) :
        t.forward(side)
        t.right(90)
 
#========================================== 
#Problem 2-3(c) 

def squareInSquare(x, y, side):
    #going to starting coordinates
    t.penup() 
    t.goto(x,y)
    t.pendown()

    def drawSquare1(x, y, side):
    #running loop 4 times to draw square
        for i in range(4) :
            t.forward(side)
            t.right(90)

    def drawTiltedSquare1(x, y, side):
        #changing the orientation of the turtle to make the square tiled
        t.right(45)
        #running loop 4 times to draw tiled square
        for i in range(4) :
            t.forward(side)
            t.right(90)

    #calling function to draw square
    drawSquare1(x, y, side)
    #moving to starting point of tiled square
    t.forward(side/2)
    #calculating length of smaller square and updating value of variable
    side = math.sqrt(2*(side/2)*(side/2))
    #calling function to draw tiled square
    drawTiltedSquare1(x, y, side)


#==========================================
#Problem 2-3(d) 

def fractal(x, y, startSide, k):
    #going to starting coordinates
    t.penup() 
    t.goto(x,y)
    t.pendown()
    def squareInSquare2(x, y, side):

        def drawSquare2(x, y, side):
            #running loop 4 times to draw square
            for i in range(4) :
                t.forward(side)
                t.right(90)

        def drawTiltedSquare2(x, y, side):
            #changing the orientation of the turtle to make the square tiled
            t.right(45)
            #running loop 4 times to draw tiled square
            for i in range(4) :
                t.forward(side)
                t.right(90)

        #calling function to draw square
        drawSquare2(x, y, side)
        #moving to starting point of tiled square
        t.forward(side/2)
        #calculating length of smaller square and storing in a variable
        side = math.sqrt(2*(side/2)*(side/2))
        #calling function to draw tiled square
        drawTiltedSquare2(x, y, side)

    #running loop to repeat fractal
    for i in range (k) :
        #calling function to draw square within a square
        squareInSquare2(x,y, startSide)
        startSide = (math.sqrt(2*(startSide/2)*(startSide/2)))
        #going to starting point of inner fractal
        t.forward(startSide/2)
        t.right(45)
        #updating length of startSide for inner fractal
        startSide = (math.sqrt(2*(startSide/2)*(startSide/2)))
        k=k-1

#========================================
#Problem 2-3(e)
 
def fractal3(x, y, startSide, k):
    #going to starting coordinates
    t.penup() 
    t.goto(x,y)
    t.pendown()

    def drawSquare3(x, y, side):
        #running loop 4 times to draw square
        for i in range(4) :
            t.forward(side)
            t.right(90)

    def drawTiltedSquare3(x, y, side):
        #tilting the turtle to an angle to make the square tiled
        t.right(45)
        #changing the orientation of the turtle to make the square tiled
        for i in range(4) :
            t.forward(side)
            t.right(90)

    def squareInSquare3(x, y, side):
        #calling function to draw square
        drawSquare3(x, y, side)
        #moving to starting point of tiled square
        t.forward(side/2)
        #calculating length of smaller square and storing in a variable
        side = math.sqrt(2*(side/2)*(side/2))
        #calling function to draw tiled square
        drawTiltedSquare3(x, y, side)

    #running loop to repeat fractal
    for i in range (k) :
        #calling function to draw square within a square
        squareInSquare3(x,y, startSide)
        startSide = (math.sqrt(2*(startSide/2)*(startSide/2)))
        #going to starting point of inner fractal
        t.forward(startSide/2)
        t.right(45)
        #updating length of startSide for inner fractal
        startSide = (math.sqrt(2*(startSide/2)*(startSide/2)))
        k=k-1
    #going to the centre of the fractal
    t.penup()
    t.right(45)
    t.forward((math.sqrt(2*(startSide/2)*(startSide/2))))
    t.pendown()

#defining function to draw spiral
def spiralOut(x, y, startLength, k):
	
	for i in range(k):
		t.forward(startLength)
		t.left(15)
		startLength +=0.2


#==========================================
#==========================================
#Extra credit

def fractal4(x, y, startSide, k):
    #going to starting coordinates
    t.penup() 
    t.goto(x,y)
    t.pendown()

    def squareInSquare4(x, y, side):

        def drawSquare4(x, y, side):
            #running loop 4 times to draw square
            for i in range(4) :
                t.forward(side)
                t.right(90)

        def drawTiltedSquare4(x, y, side):
            #changing the orientation of the turtle to make the square tiled
            t.right(45)
            #running loop 4 times to draw tiled square
            for i in range(4) :
                t.forward(side)
                t.right(90)

        #calling function to draw square
        drawSquare4(x, y, side)
        #moving to starting point of tiled square
        t.forward(side/2)
        #calculating length of smaller square and storing in a variable
        side = math.sqrt(2*(side/2)*(side/2))
        #calling function to draw tiled square
        drawTiltedSquare4(x, y, side)

    #running loop to repeat fractal
    for i in range (k) :
        #calling function to draw square within a square
        squareInSquare4(x,y, startSide)
        startSide = (math.sqrt(2*(startSide/2)*(startSide/2)))
        #going to starting point of inner fractal
        t.forward(startSide/2)
        t.right(45)
        #updating length of startSide for inner fractal
        startSide = (math.sqrt(2*(startSide/2)*(startSide/2)))
        k=k-1
    #going to the centre of the fractal
    t.penup()
    t.right(45)
    t.forward((math.sqrt(2*(startSide/2)*(startSide/2))))
    t.pendown()

#defining function to draw fibonacci spiral
#the special name given to this spiral is called "golden spiral"
def goldenspiral(x,y, startSide, k) :
    a = 0
    b = 1
    #running loop for the number of semi-circles in the spiral we want to draw
    for i in range (k) :
        c = a+b
        t.circle(c,180)
        a = b
        b = c

#===============================================
#calling all functions -

#calling  to draw square (2a)
#drawSquare(0, 0, 100)

#calling function to draw tiled square (2b)
#drawTiltedSquare(0,0,100)

#calling function to draw square in square (2c)
#squareInSquare(0,0,100)

#calling function to draw fractal (2d)
#fractal(0,0,100,3)
        
#calling functions to draw fractal and spiral (2e)
#fractal3(0,0,100,3)       
#spiralOut(0,0,2,100)

#calling function to draw fractal and golden spiral (Extra credit)
fractal4(0,0,100,3)
goldenspiral(0,0,100,10)

#===============================================
turtle.done()


