from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

screen.listen()
# when passing a function as a parameter we use it's name without parenthesis, 
# including parenthesis will cause the function that is passed to be triggered immediately
# Higher order functions are functions that take other functions as parameters

# Challenge 1: Creating Etch-A-Sketch program
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkey(key="c", fun=tim.reset)
























screen.exitonclick()