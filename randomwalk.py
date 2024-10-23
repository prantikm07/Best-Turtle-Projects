import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.pensize(10)
tim.speed("normal")

# colours = [
#   "DarkOrchid2",
#   "DeepSkyBlue",
#   "firebrick2",
#   "LawnGreen",
#   "orchid2",
#   "SpringGreen",
#   "wheat",
#   "gold",
#   "cyan2",
#   "PeachPuff"
# ]

def colours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]

for _ in range(500):
    tim.color(colours())
    tim.forward(40)
    tim.setheading(random.choice(directions))