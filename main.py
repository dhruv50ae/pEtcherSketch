import random
from turtle import Turtle, Screen

isRaceOn = False
screen = Screen()
screen.setup(height=400, width=500)
userBet = screen.textinput(title="Who will win", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
yPositions = [-70, -40, -10, 20, 50, 80]
allTurtles = []

for turtleIndex in range(0, 6):
    rammus = Turtle(shape="turtle")
    rammus.color(colours[turtleIndex])
    rammus.penup()
    rammus.goto(x=-240, y=yPositions[turtleIndex])
    allTurtles.append(rammus)

if userBet:
    isRaceOn = True

while isRaceOn:
    for turtle in allTurtles:
        if turtle.xcor() > 230:
            isRaceOn = False
            winningTurtle = turtle.pencolor()
            if winningTurtle == userBet:
                print(f"You've won! The {winningTurtle} turtle is the winner!")
            else:
                print(f"Unfortunately You've Lost. The {winningTurtle} turtle is the winner!")
        randDistance = random.randint(0, 10)
        turtle.forward(randDistance)

screen.exitonclick()