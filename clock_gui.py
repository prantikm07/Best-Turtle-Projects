import turtle
import datetime

# Create Screen
screen = turtle.Screen()
screen.title("Prantik's Analog Clock")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Draw the clock circle
clock_face = turtle.Turtle()
clock_face.speed(0)
clock_face.penup()
clock_face.pensize(5)
clock_face.goto(0, -200)
clock_face.pendown()
clock_face.circle(200)

# Add hour ticks (12 ticks)
clock_face.penup()
clock_face.goto(0, 0)
clock_face.setheading(90)

for _ in range(12):
    clock_face.penup()
    clock_face.forward(160)
    clock_face.pendown()
    clock_face.forward(20)
    clock_face.penup()
    clock_face.goto(0, 0)
    clock_face.right(30)

# Center point of the clock (small circle)
center_circle = turtle.Turtle()
center_circle.shape("circle")
center_circle.color("black")
center_circle.shapesize(0.3)

# Custom shapes for clock hands
turtle.register_shape("hour_hand", ((-5, -10), (5, -10), (3, 120), (-3, 120)))
turtle.register_shape("minute_hand", ((-3, -10), (3, -10), (2, 160), (-2, 160)))
turtle.register_shape("second_hand", ((-2, -10), (2, -10), (1, 180), (-1, 180)))

# Creating clock hands
hands = []
for shape, color in [("hour_hand", "black"), ("minute_hand", "red"), ("second_hand", "cyan")]:
    hand = turtle.Turtle()
    hand.shape(shape)
    hand.color(color)
    hand.penup()
    hand.goto(0, 0)
    hand.setheading(90)  # Pointing to 12 o'clock
    hands.append(hand)

# Function to update position of clock hands
def update_clock_hands():
    now = datetime.datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second

    # Calculate angles for each hand
    angles = [
        (hour + minute / 60) * 360 / 12,    # Hour hand
        (minute + second / 60) * 360 / 60,  # Minute hand
        (second + now.microsecond / 1000000) * 360 / 60  # Second hand
    ]

    # Align the hands based on angles
    for hand, angle in zip(hands, angles):
        hand.setheading(90 - angle)

# Create a digital time display
digital_time_display = turtle.Turtle()
digital_time_display.speed(0)
digital_time_display.penup()
digital_time_display.goto(0, 250)
digital_time_display.pendown()
digital_time_display.hideturtle()

# Function to update digital time
def update_digital_time():
    now = datetime.datetime.now()
    digital_time_display.clear()
    digital_time_display.write(now.strftime("%I:%M:%S %p"), align="center", font=("Poppins", 24, "bold"))

# Timer to update the clock and digital time every second
def update_clock():
    update_clock_hands()
    update_digital_time()
    screen.update()
    screen.ontimer(update_clock, 1000)

# Initial call to start the clock
update_clock()

# Close the turtle graphics window on click
screen.exitonclick()
turtle.bye()
