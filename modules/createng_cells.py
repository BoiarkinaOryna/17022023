import turtle

def draw_cells():
    t1.right(90)
    x = 0 
    y = 0
    for count in range(2):
        t1.penup()
        t1.goto(x, y)
        t1.pendown()
        for count in range(4):
            t1.right(90)
            t1.forward(100)
        x += 100

t1 = turtle.Turtle()
t1.hideturtle()
# draw_cells()