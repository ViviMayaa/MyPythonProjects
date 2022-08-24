from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
START_POSITION = [(00, 00), (-20, 00), (-40, 00)]


class Snake:
    def __init__(self):
        self.turtle_list = []
        self.starting_snake_body()
        self.head = self.turtle_list[0]

    def starting_snake_body(self):
        for position in range(0, 3):
            self.add_turtle(START_POSITION[position])

    def add_turtle(self, position):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape('square')
        new_turtle.color('white')
        new_turtle.goto(position)
        self.turtle_list.append(new_turtle)

    def extend(self):
        last_turtle_position = self.turtle_list[-1].position()
        self.add_turtle(last_turtle_position)

    def move(self):
        for turtle in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[turtle - 1].xcor()
            new_y = self.turtle_list[turtle - 1].ycor()
            self.turtle_list[turtle].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
