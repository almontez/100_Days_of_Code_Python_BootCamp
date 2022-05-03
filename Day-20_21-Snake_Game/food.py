from turtle import Turtle
import random


class Food(Turtle):
    """Food class with methods for moving the location of food"""

    def __init__(self):
        """Initializes shape, size, color, and location of first food item"""
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('green')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """Sets food in new random location"""
        rand_x = random.randint(-275, 275)
        rand_y = random.randint(-275, 265)
        self.goto(rand_x, rand_y)
