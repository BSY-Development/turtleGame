from turtle import Screen
import time
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkeypress(player.move_turtle, "Up")
score = Scoreboard()
car = CarManager()
game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    for cars in car.all_cars:
        car.move_car(cars)
        if cars.distance(player) < 20:
            screen.update()
            score.end_game()
            game_is_on = False
    if player.ycor() >= 280:
        player.setposition(0, -280)
        score.update_level()
        car.update_move_speed()


screen.exitonclick()
