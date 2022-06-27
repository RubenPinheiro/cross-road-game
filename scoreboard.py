from turtle import Turtle

FONT = ("Courier", 20, "bold")
ALIGN = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.speed("fastest")
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)
        self.hideturtle()
        self.move_speed = 0.1

    def refresh(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)
        self.move_speed *= 0.7

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

