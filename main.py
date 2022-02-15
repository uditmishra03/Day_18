from turtle import Turtle, Screen
import random

squirtle = Turtle()
squirtle.shape("turtle")
squirtle.color("red")
squirtle.get_shapepoly()
# ((50, -20), (30, 20), (-50, 20), (-30, -20))
# for _ in range(100):
#     squirtle.forward(500/100)
#     squirtle.penup()
#     squirtle.forward(500/100)
#     squirtle.pendown()
#     # squirtle.right(90)

no_of_sides = 0
colors = ["aqua", "salmon", "aquamarine4", "orchid", "gold", "sienna", "red", "olive", "navy", "maroon", "sandy brown"]


def draw_shape(no_of_sides):
    angle = 360 / no_of_sides
    squirtle.pencolor(chosen_color)
    for _ in range(no_of_sides):
        squirtle.forward(100)
        squirtle.right(angle)


# print(angle)
for shape_side in range(3, 11):
    chosen_color = random.choice(colors)
    draw_shape(shape_side)
    no_of_sides += 1

screen = Screen()
screen.exitonclick()
