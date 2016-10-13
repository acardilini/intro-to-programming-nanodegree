# Udacity - Intro To Programming Nanodegree
## Stage 3 Notes
---
### 3.1 Creating a Movie Website
The intention of this lesson is to learn how to use other peoples code in my own projects.

#### 3.2 Introduction to Abstration


#### 3.4 Use Classes - Draw Turtles
##### Drawing a square in python
First think about the step by step instructions that you would give to a computer to draw a square. I did:

"Take two steps forward, turn clockwise 90 degrees and take two steps, turn clockwise 90 degrees and take two steps, turn clockwise 90 degrees and take two steps"

To draw things in python we create a new python src file and write the following code.

```python
import turtle

def draw_square():
  window = turtle.Screen()
  window.bgcolor('pink')

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

```
Where:
window - creates a window for us to actually draw our turtle in, with a nice pink background.
sarah - is our turtle

#### Where do turtles come from?
Inside the python library is the file 'tutle' which contains the class 'Turtle'. A class contains a series of functions that are called when we call 'Turtle'.

When we created the class 'sarah' it was able to access all of the functions inside the 'Turtle' class include 'forward', 'right', etc.

#### Turtle information in Python docs
We can find all of the available functions for turtle objects by looking at the python documentation: https://docs.python.org/2/library/turtle.html

#### Improving code
There is repetition in the code and the name of the function is not very indicative because we are now creating multiple shapes.

We can improve the code with the following changes:
1) We can change the name to `draw_shapes()`

2) We can reduce repetition by useing a function:
```python
square = 4
while square > 1:
  sarah.forward(100)
  sarah.right(90)
  square = square - 1
```
An even better answer from the instructor is to create a generic draw_square function that can be called when needed. Such as:
```python
def draw_square(a_turtle):
  for i in range (1,5):
    a_turtle.forward(100)
    a_turtle.right(90)
```
This function is then called in the `draw.shapes()` function that I have created, e.g. `draw.square(sarah)`.

To create a triangle we could use the following code:
```python
def draw_triangle(a_turtle):
  for i in range (1,4):
    a_turtle.backward(150)
    a_turtle.left(120)
```
The instructors code is better optimised than mine because it has less lines and can be called whenever necessary. These two points are important to remember for future coding.

#### What is a class?
A class contains information that can be used to create an object, e.g. a Turtle. We can use a class to create multiple instances of the object. It's useful to think of a class as a blueprint with the objects being different buildings being created from the one blueprint.

#### Drawing a circle from squares
To create a circle made of squares we want to draw our square multiple times, but we will need to turn slightly between each square. To do this we can draw our square as normal, turn, and draw another square. The following code does this:
```python
for i in (1,37):
  draw.square(sarah)
  sarah.right(10)
```

#### Calling classes
Calling classes might look similar to calling functions but has a different outcome. For instance, when calling `turtle.Turtle()` we are calling a class which in-turn calls the class function `init` which initialises space in memory that didn't exist before.

### Use Classes - Send Texts
To do this section of the course we need to install 'twilio' a package that allows you to send phone messages.

When I first attempted to install twilio I used the following code `sudo easy_install twilio`. This did not work because my computer automatically uses version 3 of python rather than version 2. So twilio was installed on version 3 but not 2. To fix this issue I had to use the python2 version of easy_install-2.7 to install twilio, e.g. `sudo easy_install-2.7 twilio`.
