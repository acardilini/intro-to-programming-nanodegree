# Drawing a flower

import turtle

def draw_head(a_turtle):
    for i in range(1, 3):
        a_turtle.forward(50)
        a_turtle.right(30)
        a_turtle.forward(50)
        a_turtle.right(150)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("blue")

    # create turtle and walk
    sarah = turtle.Turtle()
    sarah.shape("circle")
    sarah.color("red")
    sarah.speed(50)

    for i in range(1,49):
        draw_head(sarah)
        sarah.right(7.5)

    sarah.right(90)
    sarah.forward(200)

    sarah.left(135)
    draw_head(sarah)
    sarah.left(120)
    draw_head(sarah)
    sarah.left(105)
    sarah.forward(150)

    window.exitonclick()

draw_flower()
