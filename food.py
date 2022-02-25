from turtle import Turtle
import random
from colours import colours
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.reset_position()
        self.reset_colour()

    def reset_position(self):
        x_position = random.randint(-280, 280)
        y_position = random.randint(-280, 280)
        self.goto(x_position, y_position)

    def reset_colour(self):
        rand_color = random.choice(colours)
        self.color(rand_color)



