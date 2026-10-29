from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.stage = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.stage}", align="left", font=FONT)

    def update_stage(self):
        self.stage += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)