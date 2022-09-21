from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Fira Code', 20, "normal")
FONT_BIG = ('Fira Code', 30, "bold")
SCORE_PREFIX = "Score: "
SCORE_SUFFIX = ""

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write_score()
    def write_score(self):
        self.clear()
        self.write(f'{SCORE_PREFIX}{self.score}{SCORE_SUFFIX}', False, ALIGNMENT, FONT)
    def update_score(self):
        self.score+= 1
        self.write_score()
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT_BIG)


