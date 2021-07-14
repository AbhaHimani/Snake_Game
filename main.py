import time
from food import Food
import turtle
from scoreboard import Scoreboard
from turtle import Turtle,Screen
from snake import Snake
from scoreboard import Scoreboard
screen = Screen()
food=Food()
Scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        Scoreboard.increase_score()
        snake.extend()
    #Detect Collision w wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_is_on=False
        Scoreboard.Game_Over()
    for segment in snake.segments:
            if segment != snake.head:

             if snake.head.distance(segment) < 10:
              game_is_on=False
              Scoreboard.Game_Over()

screen.exitonclick()







