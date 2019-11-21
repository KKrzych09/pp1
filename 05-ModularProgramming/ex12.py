import turtle

pen = turtle.Turtle()
screen_size = (500, 500)
pen.screen.setworldcoordinates(0, screen_size[1], screen_size[0], 0)

def draw_square(x, y, n):

    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    
    
    for _ in range(4):
        pen.forward(n)
        pen.left(90)
    pen.hideturtle()

#draw_square(200,200,100)

def draw_circle(x, y, r):

    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    for _ in range(37):
        pen.forward(r)
        pen.left(10)
    pen.hideturtle() 
    
    
#draw_circle(200, 200, 10)


def draw_triangle(x, y, m):

    pen.penup()
    pen.goto(x,y)
    pen.pendown()

    pen.left(60)
    for _ in range(3):
        pen.forward(m)
        pen.left(120)
    pen.hideturtle()

#draw_triangle(200,200,100)
    
def draw_star(x, y, a):

    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    
    for _ in range(5):
        pen.forward(a)
        pen.left(144)
        pen.forward(a)
        pen.left(72 - 144)
    
    pen.hideturtle()

#draw_star(200,200,100)

def draw_black_square(x, y, m, color):
    
    pen.fillcolor(color)
    pen.begin_fill()

    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    
    for _ in range(4):
        pen.forward(m)
        pen.left(90)
    pen.hideturtle()
    pen.end_fill()

#draw_black_square(200,200,100, "black")

def draw_chessboard_white(x, y, m):
    
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    
    pen.fillcolor("white")
    pen.begin_fill()
    
    for _ in range(4):
        pen.forward(m)
        pen.left(90)
    pen.hideturtle()
    pen.end_fill()

def draw_chessboard_black(x, y, m):
    
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    
    pen.fillcolor("black")
    pen.begin_fill()
    
    for _ in range(4):
        pen.forward(m)
        pen.left(90)
    pen.hideturtle()
    pen.end_fill()

#usun znaki '#' ponizej zeby narysowac szachownice
#for _ in range(4):
#        pen.forward(496)
#        pen.left(90)
#pen.hideturtle()
#for i in range(8):
#    for j in range(8):
#        if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0:
#            draw_chessboard_white(i * 62, j * 62, 62)
#        else:
#            draw_chessboard_black(i * 62, j * 62, 62)
        