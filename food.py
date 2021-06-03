from turtle import Turtle
import random
# from snake import Snake


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize()
        self.speed("fastest")
        self.color("blue")
        self.new_food()

    def new_food(self):
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,280)
        self.goto(random_x,random_y)
