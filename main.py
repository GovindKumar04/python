import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
carmanager = CarManager()
score = Scoreboard()

screen.onkeypress(player.r_f_destination, "w")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_cars()
    carmanager.move()
    for car in carmanager.cars:
        if car.distance(player)< 20:
            print("game over")
            game_is_on = False
    if player.finish_line():
        score.score_count()
        carmanager.speed_up()
    

screen.exitonclick()
