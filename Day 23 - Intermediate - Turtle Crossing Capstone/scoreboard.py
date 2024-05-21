from turtle import Turtle

FONT = ("Courier", 19, "bold italic")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.level = 1


        self.penup()
        self.hideturtle()
        self.goto(-275, 265)
        self.refresh_scoreboard()

    
    def update_level(self):
        self.level += 1
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over", move=False, align="center", font=FONT)


