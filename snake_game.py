from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

# Game board
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#bffb03")
screen.title("Snake Game")

# Draw small border wall on green
border = Turtle()
border.hideturtle()
border.penup()
border.color("green")
border.pensize(5)
border.goto(-300, 300)  # Top-left corner
border.pendown()

# Draw the border
for _ in range(4):
    border.forward(600)  # Move forward by the width/height of the game area
    border.right(90)

screen.tracer(0)  # delay

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# Game loop
is_game_on = True
while is_game_on:
    screen.update() # update the delay
    time.sleep(0.1) # sleep for 0.1 second
    snake.move()
    scoreboard.show_score()
    # Detect collisions with a food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        scoreboard.show_score()
    # Detect collisions with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        is_game_on = False
    # Detect collisions with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            is_game_on = False

screen.exitonclick()
