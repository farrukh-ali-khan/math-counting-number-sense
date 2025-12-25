import turtle

# Get number from user
num = int(input("Enter a number (2, 5, or 10): "))

# Setup turtle
t = turtle.Turtle()
t.speed(5)

# Star size and distance between star center and number
star_size = 40
number_offset = 50

# Function to draw a star from its center
def draw_star(center_x, center_y, size):
    t.penup()
    # Move to the top point relative to center
    t.goto(center_x, center_y + size / 2)
    t.setheading(-72)  # Point turtle in correct direction
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.penup()

# Horizontal spacing adjusted
spacing = 100  # reduced from 120 to fit stars in screen

# Draw 5 stars with numbers
for i in range(1, 6):
    multiple = num * i
    print(multiple)

    x = (i - 3) * spacing  # horizontal spacing, centered
    y = 0  # center line

    # Draw star
    draw_star(x, y, star_size)

    # Write number perfectly below star
    t.goto(x, y - number_offset)
    t.write(multiple, align="center", font=("Arial", 16, "bold"))

t.hideturtle()
turtle.done()
