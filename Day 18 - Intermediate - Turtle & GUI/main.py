# Day 18 - Turtle & GUI
from turtle import Turtle, Screen
from time import sleep
import random
from random import randint

# Understanding Turtle Graphics

tim = Turtle()

tim.shape("turtle")
tim.color("medium slate blue")
screen = Screen()

# Challenge 1 - Drawing a Square:
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Separating code - Importing & Installing Modules
# to install modules not available in Python Standard Library, type command in terminal:
# python3 -m pip install <module_name>
# import heroes
# heroes.gen


# Challenge 2 - Drawing a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()


# Challenge 3 - Drawing overlaying shapes from 3 to 10 sided
# for i in range(3, 11):
#     angle = 360 / i
#     screen.colormode(255) # change the mode to accept color range from 1 to 255
#     tim.pencolor(randint(0,255), randint(0,255), randint(0,255))

#     for _ in range(i):
#         tim.forward(100)
#         tim.left(angle)


# Challenge 4 - Drawing a Random Walk
# tim.pensize(10)
tim.speed(0)
screen.colormode(255) # change the mode to accept color range from 1 to 255

# while True:
#     tim.pencolor(randint(0,255), randint(0,255), randint(0,255))
#     tim.setheading(random.choice([0, 90, 180, 270]))

#     tim.forward(20)


# Challenge 5 - Drawing a Spirograph
tim.shape("triangle")

increment = 5
max = int(360 / increment)

for _ in range(max):
    tim.pencolor(randint(0,255), randint(0,255), randint(0,255))

    tim.circle(100)

    tim.setheading(tim.heading() + increment)




screen.exitonclick()
