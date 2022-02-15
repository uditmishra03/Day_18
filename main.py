from turtle import Turtle, Screen
import random

squirtle = Turtle()
squirtle.shape("turtle")
squirtle.color("red")
squirtle.get_shapepoly()
squirtle.speed("fastest")
screen = Screen()

# ((50, -20), (30, 20), (-50, 20), (-30, -20))
# for _ in range(100):
#     squirtle.forward(500/100)
#     squirtle.penup()
#     squirtle.forward(500/100)
#     squirtle.pendown()
#     # squirtle.right(90)

no_of_sides = 0
colors = ["aqua", "salmon", "aquamarine4", "orchid", "gold", "sienna", "red", "olive", "navy", "maroon", "sandy brown"]
direction = ["right", "left"]
directions = [0, 90, 180, 270]

exiting = True


def random_walk():
    chosen_color = random.choice(colors)
    path_direction = random.choice(direction)
    heading = random.choice(directions)
    squirtle.pencolor(chosen_color)
    squirtle.pensize(10)
    squirtle.setheading(heading)
    # if path_direction == "left":
    #     squirtle.left(90)
    # else:
    #     squirtle.right(90)
    squirtle.forward(50)
    # screen.ontimer(random_walk, 5)


for _ in range(200):
    random_walk()
screen.exitonclick()
