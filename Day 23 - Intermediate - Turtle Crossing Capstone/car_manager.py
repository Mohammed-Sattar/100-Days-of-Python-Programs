from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):

    cars = []
    car_speed = STARTING_MOVE_DISTANCE


    def __init__(self):
        global cars
        super().__init__()

        self.penup()
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250, 250))
        self.position()
        CarManager.cars.append(self)


    def move(self):
        # while True:
            self.forward(self.car_speed)

    def move_all(self):
        for car in CarManager.cars:
            car.move()
    
    def update_level(self):
        CarManager.car_speed += MOVE_INCREMENT

    def detect_collision(self, player):
        for car in CarManager.cars:
            car_x,car_y = car.position()
            player_x, player_y = player.position()

            x_diff = car_x - player_x
            y_diff = car_y - player_y

            if car.distance(player) < 20:
                return True
            
            if (y_diff <= 20 and y_diff >= -20) and (x_diff < 30 and x_diff > -30):
                return True
            
        return False