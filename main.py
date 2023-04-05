import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkey(player.move_player, "w")


game_is_on = True

while game_is_on:

    time.sleep(0.1)

    screen.update()
    scoreboard.update_scoreboard()
    car_manager.create_car()
    car_manager.car_movement()

    for car in car_manager.traffic:
        if player.distance(car) <= 21:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        scoreboard.update_level()
        car_manager.increase_car_movement()
        player.go_to_start()

screen.exitonclick()
