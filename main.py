from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=400, width=500)
userBet = screen.textinput(title="Who will win", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

yPositions = [-70, -40, -10, 20, 50, 80]

for turtleIndex in range(0, 6):
    rammus = Turtle(shape="turtle")
    rammus.color(colours[turtleIndex])
    rammus.penup()
    rammus.goto(x=-240, y=yPositions[turtleIndex])

screen.exitonclick()