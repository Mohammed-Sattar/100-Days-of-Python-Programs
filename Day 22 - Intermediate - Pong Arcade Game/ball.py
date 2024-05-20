from turtle import Turtle
import time

MOVE_SIZE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("circle")
        self.color("white")
        # self.goto(300, 300)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        time.sleep(self.move_speed)
        x, y = self.position()
        x+=self.x_move
        y+=self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.home()
        self.x_move *= -1
        self.move_speed = 0.1


        
