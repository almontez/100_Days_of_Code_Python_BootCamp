from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Snake blueprint with methods for creating the snake and moving the snake"""

    def __init__(self):
        """Initializes body of snake"""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates body of snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds segments to body of snake"""
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extends the length of snake when food eaten"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves snake forward"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Turns snake head up when up key pressed"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turns snake head down when down arrow pressed"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turns snake head left when left arrow pressed"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turns snake head right when up arrow pressed"""
        if self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)
