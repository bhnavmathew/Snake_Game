from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

 
Screen = Screen()
Screen.title("Snake Game")
Screen.bgcolor("Black")
Screen.setup(width=600, height=600)
Screen.tracer(0)


matrix = []
is_game_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

Screen.listen()
Screen.onkey(snake.d1, "Right")
Screen.onkey(snake.d2, "Up")
Screen.onkey(snake.d3, "Left")
Screen.onkey(snake.d4, "Down")
food.refresh()

border = Turtle()
border.penup()
border.goto(300, 300)
border.pendown()
border.pencolor("white")
border.right(90)
border.fd(600)
border.right(90)
border.fd(600)
border.right(90)
border.fd(600)
border.right(90)
border.fd(600)
border.hideturtle()


while is_game_on:
    Screen.update()
    time.sleep(scoreboard.speed)

    snake.moves()
    if snake.matrix[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.increase_speed()
    if snake.matrix[0].xcor() > 280 or snake.matrix[0].ycor() > 280 or snake.matrix[0].xcor() < -280 or\
            snake.matrix[0].ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    for mat in snake.matrix[1:]:
        if snake.matrix[0].distance(mat) < 10:
            is_game_on = False
            scoreboard.game_over()



Screen.exitonclick()
