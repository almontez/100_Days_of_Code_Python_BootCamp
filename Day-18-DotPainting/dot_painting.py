import turtle
import random


def draw_row():
    for dot in range(10):
        timmy.dot(15, random.choice(image_colors1))
        timmy.forward(50)


def move_left():
    timmy.left(90)
    timmy.forward(35)
    timmy.left(90)
    timmy.forward(50)


def move_right():
    timmy.right(90)
    timmy.forward(35)
    timmy.right(90)
    timmy.forward(50)


timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()

turtle.colormode(255)

image_colors1 = [(166, 155, 137), (45, 44, 31), (81, 98, 75), (136, 131, 111), (148, 165, 142),
                 (38, 53, 105), (200, 198, 170), (63, 79, 127), (117, 140, 104), (181, 201, 173),
                 (219, 229, 234), (144, 156, 176), (163, 118, 95)]

timmy.goto(-230, -150)

for row in range(5):
    draw_row()
    move_left()
    draw_row()
    move_right()


screen = turtle.Screen()
screen.exitonclick()
