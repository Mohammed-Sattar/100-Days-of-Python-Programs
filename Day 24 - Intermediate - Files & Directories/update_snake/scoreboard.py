from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 13, 'italic')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.high_score = 0 

        with open(r"Day 24 - Intermediate - Files & Directories/update_snake/data.txt", mode="r") as file:
            self.high_score = int(file.read())

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.write_scoreboard()
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.write_scoreboard()

    def update_highscore(self):
        if (self.score > self.high_score):
            self.high_score = self.score

            with open(r"Day 24 - Intermediate - Files & Directories/update_snake/data.txt", mode="w") as file:
                # file.write(str(self.high_score))
                file.write(f"{self.high_score}") # using f-string instead of the previous string conversion

    def write_scoreboard(self):
        # self.write(f"Score: {self.score}", False, align="center", font=('Helvetica', 12, 'italic'))
        self.write(f"Score: {self.score}, High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        self.clear()
        self.update_highscore()
        self.score = 0
        self.write_scoreboard()
