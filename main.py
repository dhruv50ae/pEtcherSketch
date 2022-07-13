from turtle import Turtle, Screen

rammus = Turtle()
screen = Screen()

def moveFowards():
    rammus.forward(10)

def moveBackwards():
    rammus.backward(10)

def turnLeft():
    newHeading = rammus.heading()+10
    rammus.setheading(newHeading)

def turnRight():
    newHeading = rammus.heading()-10
    rammus.setheading(newHeading)

def clear():
    rammus.clear()
    rammus.penup()
    rammus.home()
    rammus.pendown()


screen.listen()
screen.onkey(key="w", fun=moveFowards)
screen.onkey(key="s", fun=moveBackwards)
screen.onkey(key="a", fun=turnLeft)
screen.onkey(key="d", fun=turnRight)
screen.onkey(key="c", fun=clear)
screen.exitonclick()