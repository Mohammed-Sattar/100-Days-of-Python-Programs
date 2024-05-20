from turtle import Turtle
import time

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
    
    def create_snake(self):
        self.segment1 = Turtle(shape="square")
        self.segment2 = Turtle(shape="square")
        self.segment3 = Turtle(shape="square")
        self.segments = [self.segment1, self.segment2, self.segment3]

        # segment (turtle) characteristics
        for segment in self.segments:
            segment.color("white")
            segment.penup()
            segment.speed(1)

        for i in range(len(START_POSITIONS)):
            self.segments[i].goto(START_POSITIONS[i])


    def move(self):
        time.sleep(0.1)

        for segment in range(len(self.segments)-1, 0, -1):
            new_pos = self.segments[segment - 1].position()
            self.segments[segment].goto(new_pos)

        self.segment1.forward(MOVE_DISTANCE)

    def up(self):
        if self.segment1.heading() != DOWN:
            self.segment1.setheading(UP)

    def down(self):
        if self.segment1.heading() != UP:
            self.segment1.setheading(DOWN)
        
    def left(self):
        if self.segment1.heading() != RIGHT:
            self.segment1.setheading(LEFT)

    def right(self):
        if self.segment1.heading() != LEFT:
            self.segment1.setheading(RIGHT)




    def get_pos(self):
        return self.segment1.position()