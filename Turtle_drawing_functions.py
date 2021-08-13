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


def Box1_even():
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward((BOX_PLOT_MEDIAN_EVEN - BOX_PLOT_LOWER_QUARTILE_EVEN) * SIZE)
    turtle.left(90)
    turtle.forward(40*2)
    turtle.left(90)
    turtle.forward((BOX_PLOT_MEDIAN_EVEN - BOX_PLOT_LOWER_QUARTILE_EVEN) * SIZE)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)


def Box1_odd():
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward((BOX_PLOT_MEDIAN_ODD - BOX_PLOT_LOWER_QUARTILE_ODD) * SIZE)
    turtle.left(90)
    turtle.forward(40*2)
    turtle.left(90)
    turtle.forward((BOX_PLOT_MEDIAN_ODD - BOX_PLOT_LOWER_QUARTILE_ODD) * SIZE)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)


def Box2_even():
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward((BOX_PLOT_UPPER_QUARTILE_EVEN - BOX_PLOT_MEDIAN_EVEN) * SIZE)
    turtle.right(90)
    turtle.forward(40*2)
    turtle.right(90)
    turtle.forward((BOX_PLOT_UPPER_QUARTILE_EVEN - BOX_PLOT_MEDIAN_EVEN) * SIZE)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)


def Box2_odd():
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward((BOX_PLOT_UPPER_QUARTILE_ODD - BOX_PLOT_MEDIAN_ODD) * SIZE)
    turtle.right(90)
    turtle.forward(40*2)
    turtle.right(90)
    turtle.forward((BOX_PLOT_UPPER_QUARTILE_ODD - BOX_PLOT_MEDIAN_ODD) * SIZE)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)


def Box_Plot_Maker_even():
    solution_even()
    Turtle_Line_short()
    turtle.forward((BOX_PLOT_LOWER_QUARTILE_EVEN - BOX_PLOT_MIN)*SIZE)
    Box1_even()
    turtle.penup()
    turtle.forward((BOX_PLOT_MEDIAN_EVEN - BOX_PLOT_LOWER_QUARTILE_EVEN) * SIZE)
    turtle.pendown()
    Box2_even()
    turtle.penup()
    turtle.forward((BOX_PLOT_UPPER_QUARTILE_EVEN - BOX_PLOT_MEDIAN_EVEN) * SIZE)
    turtle.pendown()
    turtle.forward((BOX_PLOT_MAX - BOX_PLOT_UPPER_QUARTILE_EVEN) * SIZE)
    Turtle_Line_short()


def Box_Plot_Maker_odd():
    solution_odd()
    Turtle_Line_short()
    turtle.forward((BOX_PLOT_LOWER_QUARTILE_ODD - BOX_PLOT_MIN)*SIZE)
    Box1_odd()
    turtle.penup()
    turtle.forward((BOX_PLOT_MEDIAN_ODD - BOX_PLOT_LOWER_QUARTILE_ODD) * SIZE)
    turtle.pendown()
    Box2_odd()
    turtle.penup()
    turtle.forward((BOX_PLOT_UPPER_QUARTILE_ODD - BOX_PLOT_MEDIAN_ODD) * SIZE)
    turtle.pendown()
    turtle.forward((BOX_PLOT_MAX - BOX_PLOT_UPPER_QUARTILE_ODD) * SIZE)
    Turtle_Line_short()