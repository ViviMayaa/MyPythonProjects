from turtle import Screen
from playerturtle import Playerturtle
from cars import Cars
import time
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600
CARS_CREATED = 3
screen = Screen()
scoreboard = Scoreboard()
screen.tracer(0)
screen.colormode(255)
screen.title('Turtle Race')


screen.setup(width=WIDTH, height=HEIGHT)


screen.listen()
player_turtle = Playerturtle()
screen.onkey(player_turtle.up, "Up")
screen.onkey(player_turtle.down, "Down")


def creating_car(list_of_cars):
    for numero in range(CARS_CREATED):
        list_of_cars.append(Cars())


def turtle_game():
    running_times = 0
    level = 1
    list_of_cars = []
    times_to_run = 30 - level
    moving_speed_max = 5 + level
    game_is_on = True
    creating_car(list_of_cars)

    while game_is_on:
        screen.update()
        running_times += 1
        time.sleep(0.1)
        scoreboard.score_board(level)

        # Moving cars
        for amount in list_of_cars:
            amount.car_moving(moving_speed_max)
            if player_turtle.distance(amount) < 25 and \
                    (player_turtle.ycor() <= amount.ycor() or player_turtle.ycor() > amount.ycor()):
                scoreboard_over = Scoreboard()
                scoreboard_over.game_over()
                game_is_on = False

        # Creating new cars
        if running_times == times_to_run:
            creating_car(list_of_cars)
            running_times = 0

        # Winning and raising level
        if player_turtle.ycor() >= 300:
            level += 1
            player_turtle.goto(00, -280)


turtle_game()
screen.exitonclick()
