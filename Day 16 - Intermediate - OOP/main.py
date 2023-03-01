
import turtle

# How to Add Python Packages and use PyPi:
from prettytable import PrettyTable

# Video code - Constructing Objects and Accessing their Attributes and Methods:
timmy = turtle.Turtle()         # creating an object of name timmy from class Turtle

my_screen = turtle.Screen()     # creating an object of name my_screen from class Screen
timmy.shape("turtle")
timmy.color("DarkBlue")

print(my_screen.canvheight)     # accessing the attribute canvheight from the object
timmy.forward(100)
my_screen.exitonclick()         # accessing the exitonclick() method, this keeps the canvas open until the x is clicked


# How to Add Python Packages and use PyPi
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)