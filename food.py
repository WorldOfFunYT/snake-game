from mimetypes import init
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, colour, size):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=size, stretch_wid=size)
        self.color(colour)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        random_x = random.randint(-270, 270)
        random_x = round(random_x/28)*28
        random_y = random.randint(-270, 270)
        random_y = round(random_y/28)*28
        self.goto(random_x, random_y)