from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.update()


screen.listen()
screen.onkeypress(key="Up" ,fun=right_paddle.up)
screen.onkeypress(key="Down" ,fun=right_paddle.down)
screen.onkeypress(key="w" ,fun=left_paddle.up)
screen.onkeypress(key="s" ,fun=left_paddle.down)

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    # screen.update()
    # while (ball.xcor() < 300 and ball.ycor() < 300):
    # print(f"({x_move}, {y_move})")
    ball.move()
    screen.update()

    # Detect collision with upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # if ball.ycor() > 280:
    #     if ball.xcor() > 0:
    #         x_move = 10
    #         y_move = -10
    #     else:
    #         x_move = -10
    #         y_move = -10
    # elif ball.ycor() < -280:
    #     if ball.xcor() > 0:
    #         x_move = 10
    #         y_move = 10
    #     else:
    #         x_move = -10
    #         y_move = 10 

    #Detect collision with paddles (return serve)
    if (ball.xcor()>= 330 and right_paddle.distance(ball) <= 50) or (ball.xcor()<= -330 and left_paddle.distance(ball) <= 50):
        ball.bounce_x()

    #Detect collision with left and right walls
    if ball.xcor() < -380: 
        ball.reset_ball()
        scoreboard.r_point()

    elif ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()



screen.exitonclick()