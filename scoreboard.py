from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed = 0.3
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()


    def increase_speed(self):
        if self.score % 3 == 0:
            self.speed += 0.1

    def update_scoreboard(self):
        self.write(f"Score {self.score}", align="center", font=("Arial black", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font="normal")






