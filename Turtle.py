import turtle

# screen colour
# bgcolor = background colour
screen_colour = turtle.Screen()
screen_colour.bgcolor("green")

#Turtle colour
my_turtle = turtle.Turtle()
my_turtle.color("white")

def square(Length, Angle, second_angle):
    for i in range(4):
        my_turtle.forward(Length)
        my_turtle.right(Angle)

    my_turtle.right(second_angle)

for i in range(100):
    square(100, 90, 11)
