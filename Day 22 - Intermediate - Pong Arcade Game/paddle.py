from turtle import Turtle

MOVE_SIZE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.move_size = 20


    def up(self):
        self.forward(MOVE_SIZE)

    def down(self):
        self.backward(MOVE_SIZE)