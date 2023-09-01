from turtle import Turtle, Screen

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
Screen = Screen()


class Snake:
    def __init__(self):
        self.matrix = []
        self.create_snake()


    def create_snake(self):
        for i in range(0, 3):
            self.add_segments(COORDINATES[i])


    def extend(self):
        self.add_segments(self.matrix[-1].position())

    def add_segments(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.matrix.append(snake)

    def moves(self):
        for mat in range(len(self.matrix) - 1, 0, -1):
            new_x = self.matrix[mat - 1].xcor()
            new_y = self.matrix[mat - 1].ycor()
            self.matrix[mat].goto(new_x, new_y)
        self.matrix[0].fd(MOVE_DISTANCE)

    def d1(self):
        if self.matrix[0].heading() != 180:
            self.matrix[0].setheading(0)

    def d2(self):
        if self.matrix[0].heading() != 270:
            self.matrix[0].setheading(90)

    def d3(self):
        if self.matrix[0].heading() != 0:
            self.matrix[0].setheading(180)

    def d4(self):
        if self.matrix[0].heading() != 90:
            self.matrix[0].setheading(270)
