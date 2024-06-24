from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer(0)


r_paddle = Paddle((380, 0))
l_paddle = Paddle((-390, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # Detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    # Detect Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect R paddle misses or L paddle misses
    if ball.xcor() > 390:
        ball.rev_bounce()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.rev_bounce()
        scoreboard.r_point()









screen.exitonclick()
