COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
import time

class CarManager():
    def __init__(self):
        self.cars = []
    def create_cars(self):
        if random.randint(1,6)==1:
            self.car = Turtle()
            self.car.color(random.choice(COLORS))
            self.car.shape("square")
            self.car.penup()
            self.car.shapesize(stretch_wid=1, stretch_len=3)
            self.car.goto(300,random.randint(-250,250))
            self.cars.append(self.car)
            self.move_d = STARTING_MOVE_DISTANCE
    def move(self):
        for car in self.cars:
            car.backward(self.move_d)
    def speed_up(self):
        self.move_d += MOVE_INCREMENT
                   


        
        
