# Day 18 Project - Drawing a Hirst Spot Painting with Random Colors

import colorgram
import turtle
from turtle import Turtle, Screen
import random

def color_extraction(num_of_colors):
    colors = colorgram.extract('Day 18 - Intermediate - Turtle & GUI/Ellipticine.jpg', num_of_colors)

    rgb_list = []

    for color in colors:
        color_tuple = color.rgb

        # color_red_value = color_tuple[0]
        # color_green_value = color_tuple[1]
        # color_blue_value = color_tuple[2]

        # color_tuple = (color_red_value, color_green_value, color_blue_value)

        # removes the lighter colors that are most likely background colors
        if (color_tuple[0] > 200 and color_tuple[1] > 200 and color_tuple[2] > 200):
            continue
        
        rgb_list.append(color_tuple)
    
    return rgb_list



tim = Turtle()

tim.speed(0)
tim.penup()
tim.hideturtle()
turtle.colormode(255) # change the mode to accept color range from 1 to 255
colors = color_extraction(30)

for y_coordinate in range(-200, 300, 50):
    tim.setpos(-200, y_coordinate)

    for _ in range(10):
        tim.dot(20, random.choice(colors))
        tim.forward(50)



screen = Screen()
screen.exitonclick()

