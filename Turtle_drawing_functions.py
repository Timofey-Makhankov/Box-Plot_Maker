import turtle
# Makes a Horizontal Line for each Size
def Turtle_Line_short():
    turtle.left(90)
    turtle.forward(20)
    turtle.left(180)
    turtle.forward(20*2)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(90)

def turtle_Line_shorter():
    turtle.left(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(10*2)
    turtle.left(180)
    turtle.forward(10)
    turtle.right(90)

def turtle_Line_shortest():
    turtle.left(90)
    turtle.forward(5)
    turtle.left(180)
    turtle.forward(5*2)
    turtle.left(180)
    turtle.forward(5)
    turtle.right(90)


# Creates one of the Squares to the left 
def Box1_even(median, lower_quartile, size):
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward((median - lower_quartile) * size)
    turtle.left(90)
    turtle.forward(40*2)
    turtle.left(90)
    turtle.forward((median - lower_quartile) * size)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)


def Box1_odd(median: float, lower_quartile:float, size: int):
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward((median - lower_quartile) * size)
    turtle.left(90)
    turtle.forward(40*2)
    turtle.left(90)
    turtle.forward((median - lower_quartile) * size)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)


# Creates one of the Squares to the right
def Box2_even(upper_quartile, median, size):
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward((upper_quartile - median) * size)
    turtle.right(90)
    turtle.forward(40*2)
    turtle.right(90)
    turtle.forward((upper_quartile - median) * size)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)


def Box2_odd(upper_quartile, median, size):
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward((upper_quartile - median) * size)
    turtle.right(90)
    turtle.forward(40*2)
    turtle.right(90)
    turtle.forward((upper_quartile - median) * size)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)