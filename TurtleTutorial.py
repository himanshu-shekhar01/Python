# Python program to draw square 

# import turtle
# skk = turtle.Turtle()
# for i in range(4):
#     skk.forward(100)
#     skk.right(120)

# turtle.done()

# Python program to draw star

# import turtle
# star = turtle.Turtle()

# star.right(75)
# star.forward(100)

# for i in range(4):
#     star.right(144)
#     star.forward(100)
    
# turtle.done()


# import turtle

# # Set up the turtle screen and set the background color to white
# screen = turtle.Screen()
# screen.bgcolor("green")

# # Create a new turtle and set its speed to the fastest possible
# pen = turtle.Turtle()

# # Set the fill color to red
# pen.fillcolor("white")
# pen.begin_fill()

# # Draw the circle with a radius of 100 pixels
# pen.circle(100)

# # End the fill and stop drawing
# pen.end_fill()
# pen.hideturtle()

# # Keep the turtle window open until it is manually closed
# turtle.done()

# Python program to user input pattern
# using Turtle Programming
import turtle   #Outside_In
import turtle
import time
import random

print ("This program draws shapes based on the number you enter in a uniform pattern.")
num_str = input("Enter the side number of the shape you want to draw: ")
if num_str.isdigit():
    squares = int(num_str)

angle = 180 - 180*(squares-2)/squares

turtle.up

x = 0 
y = 0
turtle.setpos(x, y)


numshapes = 8
for x in range(numshapes):
    turtle.color(random.random(), random.random(), random.random())
    x += 5
    y += 5
    turtle.forward(x)
    turtle.left(y)
    for i in range(squares):
        turtle.begin_fill()
        turtle.down()
        turtle.forward(40)
        turtle.left(angle)
        turtle.forward(40)
        print (turtle.pos())
        turtle.up()
        turtle.end_fill()

time.sleep(11)
turtle.bye()