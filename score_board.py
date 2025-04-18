from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
    def increase_score(self):
        self.score += 1
    def clear_score(self):
        self.score = 0
    def show_score(self):
        self.clear()
        self.penup()
        self.goto(0, 265)
        self.color("black")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)