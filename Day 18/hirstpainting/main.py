import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(238, 234, 84), (205, 159, 104), (115, 178, 203), (31, 114, 162), (173, 16, 68), (215, 131, 164), (175, 169, 32), (159, 80, 40), (225, 55, 100), (175, 48, 92), (133, 183, 149), (14, 30, 70), (37, 131, 83), (230, 77, 50), (235, 164, 192), (228, 227, 7), (14, 49, 28), (73, 14, 54), (33, 164, 200), (26, 44, 127), (58, 165, 98), (138, 213, 226), (14, 97, 59), (79, 27, 12), (131, 34, 23), (161, 210, 182), (230, 171, 161), (11, 90, 104), (180, 185, 214), (103, 88, 13), (95, 123, 177), (254, 3, 80)]
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 101

for dot_count in range(1, number_of_dots):
    tim.hideturtle()
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    tim.speed("fastest")
    if dot_count % 10 == 0:

        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




















screen = turtle_module.Screen()
screen.exitonclick()
