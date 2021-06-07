import time
from turtle import Screen, Turtle
from Day23_1_player import Player
from Day23_1_car_manager import CarManager
from Day23_1_scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
road = Turtle("square")
road.color("light gray")
road.shapesize(25, 30, 1)
scoreboard = Scoreboard()
player = Player()
manager = CarManager()
screen.listen()
screen.onkey(fun=player.move, key="Up")
difficulty = 0.1

game_is_on = True
cycle = 0
while game_is_on:
    while cycle == 6:
        manager.generate()
        cycle = 0
    time.sleep(difficulty)
    screen.update()
    manager.travel()
    cycle += 1

    if player.reach_goal():
        scoreboard.level_up()
        difficulty *= 0.6

    for car in manager.car_list:
        if 20 > car.xcor() > -20:
            if player.distance(car) < 15:
                scoreboard.game_over()
                game_is_on = False

screen.exitonclick()
