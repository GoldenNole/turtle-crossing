from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.traffic = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            rand_y = randint(-250, 250)
            new_car.goto(310, rand_y)
            self.traffic.append(new_car)

    def car_movement(self):
        for car in self.traffic:
            car.backward(self.car_speed)

    def increase_car_movement(self):
        self.car_speed += MOVE_INCREMENT
