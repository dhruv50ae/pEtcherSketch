from turtle import Turtle, Screen

rammus = Turtle()
screen = Screen()

def moveFowards():
    rammus.forward(10)

screen.listen()
screen.onkey(key="space", fun=moveFowards)
screen.exitonclick()