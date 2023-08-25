FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.s_count = 0
        self.goto(-250,250)
        self.score_count()
    def score_count(self):
        self.clear()
        self.write(arg=f"Score {self.s_count}", font=FONT)
        self.s_count += 1
       