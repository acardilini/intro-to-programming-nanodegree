import turtle

def draw_square():
    # open window
    window = turtle.Screen()
    window.bgcolor("gold")

    # create turtle and walk
    sarah = turtle.Turtle()
    sarah.shape("circle")
    sarah.color("red")
    sarah.speed(2)

    sarah.forward(100)
    sarah.right(90)
    sarah.forward(100)
    sarah.right(90)
    sarah.forward(100)
    sarah.right(90)
    sarah.forward(100)
    sarah.right(90)

    window.exitonclick()

draw_square()
