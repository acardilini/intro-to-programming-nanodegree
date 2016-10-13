import turtle

def draw_square(a_turtle):
    for i in range(1, 5):
        a_turtle.forward(100)
        a_turtle.right(90)

def draw_shapes():
    # open window
    window = turtle.Screen()
    window.bgcolor("blue")

    # create turtle and walk
    sarah = turtle.Turtle()
    sarah.shape("circle")
    sarah.color("red")
    sarah.speed(15)

    for i in range(1,37):
        draw_square(sarah)
        sarah.right(10)

    window.exitonclick()

draw_shapes()
