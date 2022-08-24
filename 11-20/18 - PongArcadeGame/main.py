from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard


POSITION_RIGHT = (350, 00)
POSITION_LEFT = (-350, 00)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(POSITION_RIGHT)
left_paddle = Paddle(POSITION_LEFT)
ball = Ball()
right_score = 0
left_score = 0
tim_the_worker = Scoreboard()
tim_the_worker.build_middle_line()

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')
game_is_on = True

while game_is_on:
    sleep(0.1)
    screen.update()
    ball.ball_move()
    ball.touch_paddle((right_paddle.xcor(), right_paddle.ycor()))
    ball.touch_paddle((left_paddle.xcor(), left_paddle.ycor()))



screen.exitonclick()
