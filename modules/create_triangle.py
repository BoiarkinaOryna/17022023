import turtle

def draw_triangle():
    t3.penup()
    t3.goto(75, 25)
    t3.pendown()
    for count in range(3):
        t3.left(120)
        t3.forward(50)

t3 = turtle.Turtle()
t3.hideturtle()
# draw_triangle(0, 0)