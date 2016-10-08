import turtle

# Beggining turtle
def draw_square():
    # open window
    window = turtle.Screen()
    window.bgcolor("pink")

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

    jen = turtle.Turtle()
    jen.shape("turtle")
    jen.color("gold")
    jen.speed(3)

    jen.circle(111)

    window.exitonclick()

draw_square()

# Optimised turtle
def draw_shapes():
    # open window
    window = turtle.Screen()
    window.bgcolor("pink")

    # create turtle and walk
    sarah = turtle.Turtle()
    sarah.shape("circle")
    sarah.color("red")
    sarah.speed(2)

    square = 4
    while square > 0:
      sarah.forward(100)
      sarah.right(90)
      square = square - 1

    jen = turtle.Turtle()
    jen.shape("turtle")
    jen.color("gold")
    jen.speed(3)

    jen.circle(111)

    beth = turtle.Turtle()
    beth.shape('arrow')
    beth.color('white')
    beth.speed(4)

    triangle = 3
    while triangle > 0:
      beth.backward(150)
      beth.left(120)
      triangle = triangle - 1

    window.exitonclick()

draw_shapes()
