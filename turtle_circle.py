#circle with turtle
import turtle                 #Sets up tuttle library
circle = turtle.Turtle()
wn = turtle.Screen()          #Creates a graphics window
wn.bgcolor("yellow")          #creates a background colour yellow

line=1                        #Attributes to draw a circle
angle =1

for _ in range(360):          #Using for loop 
    circle.forward(line)
    circle.left(angle)
exitonclick()
