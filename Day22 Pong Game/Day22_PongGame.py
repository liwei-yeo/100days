from turtle import Screen, Turtle
from Day22_1_paddle import Paddle
from Day22_1_ball import Ball
from Day22_1_scoreboard import Scoreboard
import time

STARTING_POS = [(350, 0), (-350, 0)]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PyPong")
screen.tracer(0)

r_paddle = Paddle(STARTING_POS[0])
l_paddle = Paddle(STARTING_POS[1])

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

scoreboard = Scoreboard()
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed_up()

    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()
