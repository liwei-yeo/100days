from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.level_string = f"Level: {self.level}"
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=self.level_string, align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.level_string = f"Level: {self.level}"
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)