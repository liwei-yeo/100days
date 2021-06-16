import time
from turtle import Screen
from Day20_21_snake import Snake
from Day20_21_food import Food
from Day20_21_scoreboard import Scoreboard

# decimal between 0 - 2, smaller is more difficulty
DIFFICULTY = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake the Python")


# turn off tracer and manually update snake movement
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.score_refresh()
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
    time.sleep(DIFFICULTY)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        scoreboard.reset_score()
        snake.reset()

    # Detect collision with tail
    for segment in snake.snake_list[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset_score()
            snake.reset()

screen.exitonclick()