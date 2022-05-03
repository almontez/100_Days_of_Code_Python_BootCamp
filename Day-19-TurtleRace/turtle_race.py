import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (ROYGBIV): ")
is_race_on = False

turtle_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
race_turtles = []
y_pos = - 150

for index in range(7):
    new_turtle = turtle.Turtle(shape='turtle')
    new_turtle.color(turtle_colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-215, y=y_pos)
    y_pos += 50

    race_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in race_turtles:
        if turtle.xcor() > 215:
            is_race_on = False

            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

screen.exitonclick()
