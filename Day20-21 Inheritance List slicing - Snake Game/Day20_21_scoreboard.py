from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

with open("Day20_21_highscore.txt") as scorefile:
    highscore = scorefile.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = int(highscore)
        self.color("yellow3")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.score_refresh()

    def score_refresh(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.score_refresh()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day20_21_highscore.txt", mode="w") as update_score:
                update_score.write(str(self.high_score))
        self.score = 0
        self.score_refresh()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)