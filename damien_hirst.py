import colorgram
import turtle as t
import random

# rgb_colors = []
# colors = colorgram.extract("new.jpg", 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color =(r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

colors = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (40, 132, 77), (128, 219, 232), (58, 12, 25), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()

tim.penup()
tim.setheading(225)
tim.forward(350)
tim.setheading(0)

for i in range(15):
    for _ in range(15):
        tim.penup()
        tim.forward(30)
        tim.dot(10, random.choice(colors))
    tim.setheading(90)
    tim.forward(30)
    tim.setheading(180)
    tim.forward(450)
    tim.setheading(0)
        

screen = t.Screen()
screen.exitonclick()