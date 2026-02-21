# import turtle
# pen = turtle.Turtle()
# pen.speed(0) 

# # Draw a square
# for _ in range(4):
#     pen.forward(100)
#     pen.left(90)

# turtle.done()

# import turtle

# screen = turtle.Screen()
# pen = turtle.Turtle()
# pen.speed(0)

# # Draw a square
# for i in range(4):
#     pen.forward(100)
#     pen.right(90)

# # Keep the window open
# pen.hideturtle()
# turtle.done()

# import turtle

# # Setup the screen
# screen = turtle.Screen()
# screen.bgcolor("white")
# pen = turtle.Turtle()
# pen.pensize(4)
# pen.speed(3)

# # Function to draw head
# def draw_head():
#     pen.penup()
#     pen.goto(0, 0)
#     pen.setheading(0)
#     pen.forward(0)
#     pen.pendown()
#     pen.circle(50)  # head

# # Function to draw body
# def draw_body():
#     pen.penup()
#     pen.goto(0, 0)
#     pen.setheading(-90)
#     pen.forward(50)
#     pen.pendown()
#     pen.forward(100)  # body

# # Function to draw arms
# def draw_arms():
#     pen.penup()
#     pen.goto(0, -50)
#     pen.setheading(-150)
#     pen.pendown()
#     pen.forward(70)  # left arm

#     pen.penup()
#     pen.goto(0, -50)
#     pen.setheading(-30)
#     pen.pendown()
#     pen.forward(70)  # right arm

# # Function to draw legs
# def draw_legs():
#     pen.penup()
#     pen.goto(0, -150)
#     pen.setheading(-120)
#     pen.pendown()
#     pen.forward(70)  # left leg

#     pen.penup()
#     pen.goto(0, -150)
#     pen.setheading(-60)
#     pen.pendown()
#     pen.forward(70)  # right leg

# # Draw the figure
# draw_head()
# draw_body()
# draw_arms()
# draw_legs()

# # Hide turtle and finish
# pen.hideturtle()
# screen.mainloop()


# import turtle
# import colorsys

# # Setup screen
# screen = turtle.Screen()
# screen.bgcolor("black")
# pen = turtle.Turtle()
# pen.speed(0)  # fastest drawing
# pen.width(2)

# # Function to draw colorful rangoli
# def draw_rangoli():
#     num_colors = 36
#     hue = 0
#     for i in range(360):
#         # Change color
#         color = colorsys.hsv_to_rgb(hue, 1, 1)
#         pen.color(color)
#         hue += 1/num_colors
        
#         pen.forward(i * 3 / num_colors + i)
#         pen.left(59)
#         pen.forward(i * 3 / num_colors + i)
#         pen.left(60)
#         pen.left(20)

# # Start drawing
# draw_rangoli()

# pen.hideturtle()
# turtle.done()


# import turtle

# # Set up screen
# screen = turtle.Screen()
# screen.bgcolor("skyblue")
# pen = turtle.Turtle()
# pen.speed(3)

# # Function to draw square
# def draw_square(color, x, y, size):
#     pen.penup()
#     pen.goto(x, y)
#     pen.pendown()
#     pen.color(color)
#     pen.begin_fill()
#     for _ in range(4):
#         pen.forward(size)
#         pen.left(90)
#     pen.end_fill()

# # Function to draw triangle (roof)
# def draw_triangle(color, x, y, size):
#     pen.penup()
#     pen.goto(x, y)
#     pen.pendown()
#     pen.color(color)
#     pen.begin_fill()
#     for _ in range(3):
#         pen.forward(size)
#         pen.left(120)
#     pen.end_fill()

# # Function to draw rectangle (door)
# def draw_rectangle(color, x, y, width, height):
#     pen.penup()
#     pen.goto(x, y)
#     pen.pendown()
#     pen.color(color)
#     pen.begin_fill()
#     for _ in range(2):
#         pen.forward(width)
#         pen.left(90)
#         pen.forward(height)
#         pen.left(90)
#     pen.end_fill()

# # Draw main house square
# draw_square("yellow", -100, -100, 200)

# # Draw roof
# draw_triangle("brown", -100, 100, 200)

# # Draw door
# draw_rectangle("red", -30, -100, 60, 100)

# # Draw windows
# draw_square("white", -90, 0, 40)
# draw_square("white", 50, 0, 40)

# # Hide turtle and finish
# pen.hideturtle()
# screen.mainloop()


# import turtle

# screen = turtle.Screen()
# screen.bgcolor("skyblue")

# t = turtle.Turtle()
# t.speed(0)
# t.pensize(2)

# # Function to draw rectangle
# def draw_rectangle(x, y, width, height, color):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.color(color)
#     t.begin_fill()
#     for _ in range(2):
#         t.forward(width)
#         t.left(90)
#         t.forward(height)
#         t.left(90)
#     t.end_fill()

# # Function to draw triangle (roof)
# def draw_triangle(x, y, width, height, color):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.color(color)
#     t.begin_fill()
#     t.goto(x + width / 2, y + height)
#     t.goto(x + width, y)
#     t.goto(x, y)
#     t.end_fill()

# # Function to draw circle (for faces, sun etc.)
# def draw_circle(x, y, radius, color):
#     t.penup()
#     t.goto(x, y - radius)
#     t.pendown()
#     t.color(color)
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()

# # Draw House
# draw_rectangle(-250, -100, 200, 150, "orange")     # House base
# draw_triangle(-250, 50, 200, 100, "brown")          # Roof
# draw_rectangle(-200, -100, 40, 70, "darkblue")      # Door
# draw_rectangle(-240, -10, 30, 30, "lightblue")      # Window
# draw_rectangle(-130, -10, 30, 30, "lightblue")      # Window

# # Draw Tree
# draw_rectangle(150, -100, 20, 60, "saddlebrown")    # Tree trunk
# t.color("forestgreen")
# t.penup()
# t.goto(160, -40)
# t.pendown()
# t.begin_fill()
# t.circle(40)
# t.end_fill()

# # Draw River
# t.penup()
# t.goto(-400, -150)
# t.color("blue")
# t.begin_fill()
# t.pendown()
# t.goto(400, -150)
# t.goto(400, -300)
# t.goto(-400, -300)
# t.goto(-400, -150)
# t.end_fill()

# # Draw Man
# draw_circle(-50, -30, 10, "peachpuff")              # Head
# draw_rectangle(-55, -80, 10, 30, "blue")            # Body
# draw_rectangle(-45, -80, 10, 30, "blue")            # Body other half

# # Draw Woman
# draw_circle(-10, -30, 10, "peachpuff")              # Head
# draw_rectangle(-15, -80, 30, 30, "pink")            # Body

# # Draw Two Kids Playing
# # Kid 1
# draw_circle(50, -40, 6, "peachpuff")                # Head
# draw_rectangle(45, -70, 10, 20, "green")            # Body

# # Kid 2
# draw_circle(80, -40, 6, "peachpuff")                # Head
# draw_rectangle(75, -70, 10, 20, "yellow")           # Body

# # Add a sun
# draw_circle(250, 180, 30, "yellow")

# t.hideturtle()
# turtle.done()
