from turtle import Screen, Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1, 1)
        self.goto(pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        # screen.update()

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        # screen.update()
