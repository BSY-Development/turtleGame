from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-220, 260)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level {self.level}", align="center", font=FONT)
        self.level += 1

    def end_game(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 30, "normal"))