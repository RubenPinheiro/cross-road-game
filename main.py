import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_list = []
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
count = 0
while game_is_on:
    time.sleep(scoreboard.move_speed)
    screen.update()

    if count % 4 == 0:
        car_list.append(CarManager())

    for car in car_list:
        car.move()
        if player.distance(car) < 15:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        scoreboard.refresh()
        player.goto(0, -280)

    count += 1

screen.exitonclick()
