from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False

tim = Turtle(shape="turtle")
kim = Turtle(shape="turtle")
lim = Turtle(shape="turtle")
jim = Turtle(shape="turtle")
jon = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
turtles = [tim, kim, lim, jim, jon, tom]


position = -125
for turtle in turtles:
    color_choice = random.choice(colors)
    turtle.color(color_choice)
    colors.remove(color_choice)
    turtle.penup()
    turtle.goto(x=-230, y=position)
    position += 50

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            is_race_on = False

            if user_bet == turtle.pencolor():
                print(f"You won! The {turtle.pencolor()} turtle won the race!")
            else:
                print(f"You lost! The {turtle.pencolor()} turtle won the race!")






screen.exitonclick()