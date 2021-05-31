from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_list = []
        self.generate()
        self.head = self.snake_list[0]

    def generate(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_list.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_list[-1].pos())

    def move(self):
        # starting from last segment, goto the previous segment
        for seg in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[seg - 1].xcor()
            new_y = self.snake_list[seg - 1].ycor()
            self.snake_list[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)