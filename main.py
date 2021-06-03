from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
COLLISION=0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake_obj = Snake()
food_obj=Food()
score_board_obj=ScoreBoard()
screen.listen()
screen.onkey(snake_obj.up, "Up")
screen.onkey(snake_obj.down, "Down")
screen.onkey(key='Left',  fun= snake_obj.left)
screen.onkey(key='Right',  fun= snake_obj.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake_obj.move_snake()

    # Detect Collision with Food
    if snake_obj.head.distance(food_obj)<15:
        food_obj.new_food()
        snake_obj.extend()
        # print("Collision")
        score_board_obj.increase_score()

    # Detect Collision with any of 4 Walls
    if snake_obj.head.xcor() >280 or snake_obj.head.xcor() <-280 or snake_obj.head.ycor() >280 or snake_obj.head.ycor() <-280:
        score_board_obj.reset_score()
        snake_obj.reset()
        COLLISION=COLLISION+1
        if COLLISION==5:
            game_is_on=False
            score_board_obj.game_over()
        # game_is_on=False

    # Detect Collision with Own
    for segment in snake_obj.segments[1:]:

        if snake_obj.head.distance(segment) <10:

            # game_is_on=False
            score_board_obj.reset_score()
            snake_obj.reset()
            if COLLISION == 3:
                game_is_on = False
                score_board_obj.game_over()

screen.exitonclick()
