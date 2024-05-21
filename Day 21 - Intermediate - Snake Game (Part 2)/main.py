from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # turns off the automatic updating of turtle's state

is_game_on = False

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

is_game_on = True
while is_game_on:
    screen.update()
    snake.move()

    # Detect collision with food
    if snake.segment1.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if snake.segment1.xcor() > 285 or snake.segment1.xcor() < -285 or snake.segment1.ycor() > 285 or snake.segment1.ycor() < -285:
        is_game_on = False
        scoreboard.game_over()

    # Detect collision with body
    for segment in snake.segments[1:]:
        if snake.segment1.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()



screen.exitonclick()