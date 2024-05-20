from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 13, 'italic')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score=0

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.write_scoreboard()
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.write_scoreboard()

    def write_scoreboard(self):
        # self.write(f"Score: {self.score}", False, align="center", font=('Helvetica', 12, 'italic'))
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, align=ALIGNMENT, font=FONT)