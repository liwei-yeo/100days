from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []

    def generate(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(1, 2, 1)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randint(-12, 12)*20)
        self.car_list.append(new_car)

    def travel(self):
        for car in self.car_list:
            new_x = car.xcor() - MOVE_INCREMENT
            car.goto(new_x, car.ycor())
            if new_x < -300:
                car.color("black")
                self.car_list.remove(car)
