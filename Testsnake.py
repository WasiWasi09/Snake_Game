from turtle import Screen,Turtle
import time
from snake import Snake
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake_obj=Snake()
# snake_obj.move_snake()
# This piece of code only moves first block to left but rest twoblock will move forward
#it will not turn left
# game_is_on=True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     for seg in segments:
#         # seg.penup()
#         seg.forward(20)
#     segments[0].left(90)
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake_obj.move_snake()






screen.exitonclick()
