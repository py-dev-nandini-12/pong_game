from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(r_paddle.mov_up, "Up")
screen.onkey(r_paddle.mov_down, "Down")
screen.onkey(l_paddle.mov_up, "w")
screen.onkey(l_paddle.mov_down, "s")

is_on = True
while is_on:
    time.sleep(ball.mov_speed)
    screen.update()
    ball.move()
    #detect collision
    if ball.ycor() < -280 or ball.ycor() >280:
        #it should bounce
        ball.bounce_y()
    #detect collision with paddle
    if ball.distance(r_paddle) <50 and ball.xcor() >320 or ball.distance(l_paddle) <50 and -320 > ball.xcor():
        ball.bounce_x()
    #right paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        score.increase_l_score()

    # left paddle misses
    if ball.xcor() < -380:
        ball.reset_pos()
        score.increase_r_score()






screen.exitonclick()
