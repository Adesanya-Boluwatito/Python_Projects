from turtle import Turtle
with open("data.txt") as data:
    highscore = int(data.read())

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.score = 0
        self.high_score = highscore
        self.goto(x=0, y=260)
        self.update_score_count()

    def update_score_count(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score} ", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score_count()

    def score_count(self):
        self.score += 1
        self.clear()
        self.update_score_count()

