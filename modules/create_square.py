import turtle

def draw_square():
    t2.penup()
    t2.goto(-25, 25)
    t2.pendown()
    for count in range(4):
            t2.left(90)
            t2.forward(50)

t2 = turtle.Turtle()
t2.hideturtle()
# draw_square(0, 0)