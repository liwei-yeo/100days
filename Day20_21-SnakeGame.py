import time
from turtle import Turtle, Screen
from Day20_21_snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake the Python")
# turn off tracer and manually update snake movement
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    # only update the snake image between each loop, to make image more smooth
    screen.update()
    # reduce time between updates
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
