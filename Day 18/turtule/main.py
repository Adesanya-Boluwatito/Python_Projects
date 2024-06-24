import turtle as t
from turtle import Turtle, Screen
import random


tim = Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")

direction = [0, 90, 180, 270]


def draw_spiral(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spiral(5)








tim.pensize(15)
tim.speed("fastest")
# for _ in range(500):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))








# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.left(angle)
#
#
# for shape_side in range(3, 11):
#     tim.color(random.choice(colour))
#     draw_shapes(shape_side)













screen = Screen()
screen.exitonclick()



