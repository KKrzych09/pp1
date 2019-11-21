import turtle
def draw_square(x,y,n):
    pen = turtle.Turtle()
    screen_size = (500, 500)
    pen.screen.setworldcoordinates(0, screen_size[1], screen_size[0], 0)

    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    for _ in range(4):
        pen.forward(n)
        pen.left(90)
    pen.hideturtle()
