import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=player.up)

game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    car.move_all()
    screen.update()

    if (loop_count % 6) == 1:
        CarManager()

    # Detect if a car collided with the player
    if car.detect_collision(player):
        game_is_on = False
        scoreboard.game_over()

    # Detect if player successfully passed all cars
    if player.ycor() > 280:
        player.update_level()
        car.update_level()
        scoreboard.update_level()


    loop_count+=1



screen.exitonclick()