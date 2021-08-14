import turtle
from functions_calculation import *
from Turtle_drawing_functions import *

with open('input.txt', encoding='utf-8') as f:
    CONTENT = f.read()
    f.close()

def get_int_list(array: str):
    string_array = array.split(" ")
    int_array = [float(n) for n in string_array]
    return int_array


int_list = get_int_list(CONTENT)
int_list_sorted = sorted(int_list)
list_length = len(int_list)

# Makes the Diagram bigger
SIZE = 10

BOX_PLOT_MIN = item_min(int_list_sorted)
BOX_PLOT_LOWER_QUARTILE_ODD = lower_quartile_odd(int_list_sorted)
BOX_PLOT_LOWER_QUARTILE_EVEN = lower_quartile_even(int_list_sorted)
BOX_PLOT_MEDIAN_ODD = median_odd(int_list_sorted, list_length)
BOX_PLOT_MEDIAN_EVEN = median_even(int_list_sorted, list_length)
BOX_PLOT_UPPER_QUARTILE_ODD = upper_quartile_odd(int_list_sorted)
BOX_PLOT_UPPER_QUARTILE_EVEN = upper_quartile_even(int_list_sorted)
BOX_PLOT_MAX = item_max(int_list_sorted)


def Box_Plot_Maker_even():
    Turtle_Line_short()
    turtle.forward((BOX_PLOT_LOWER_QUARTILE_EVEN - BOX_PLOT_MIN)*SIZE)
    Box1_even(BOX_PLOT_MEDIAN_EVEN, BOX_PLOT_LOWER_QUARTILE_EVEN, SIZE)
    turtle.penup()
    turtle.forward((BOX_PLOT_MEDIAN_EVEN - BOX_PLOT_LOWER_QUARTILE_EVEN) * SIZE)
    turtle.pendown()
    Box2_even(BOX_PLOT_UPPER_QUARTILE_EVEN, BOX_PLOT_MEDIAN_EVEN, SIZE)
    turtle.penup()
    turtle.forward((BOX_PLOT_UPPER_QUARTILE_EVEN - BOX_PLOT_MEDIAN_EVEN) * SIZE)
    turtle.pendown()
    turtle.forward((BOX_PLOT_MAX - BOX_PLOT_UPPER_QUARTILE_EVEN) * SIZE)
    Turtle_Line_short()


def Box_Plot_Maker_odd():
    Turtle_Line_short()
    turtle.forward((BOX_PLOT_LOWER_QUARTILE_ODD - BOX_PLOT_MIN)*SIZE)
    Box1_odd(BOX_PLOT_MEDIAN_ODD, BOX_PLOT_LOWER_QUARTILE_ODD, SIZE)
    turtle.penup()
    turtle.forward((BOX_PLOT_MEDIAN_ODD - BOX_PLOT_LOWER_QUARTILE_ODD) * SIZE)
    turtle.pendown()
    Box2_odd(BOX_PLOT_UPPER_QUARTILE_ODD, BOX_PLOT_MEDIAN_ODD, SIZE)
    turtle.penup()
    turtle.forward((BOX_PLOT_UPPER_QUARTILE_ODD - BOX_PLOT_MEDIAN_ODD) * SIZE)
    turtle.pendown()
    turtle.forward((BOX_PLOT_MAX - BOX_PLOT_UPPER_QUARTILE_ODD) * SIZE)
    Turtle_Line_short()


# Prints the Result in the Terminal
def solution_even():
    print(f"Das Zentral Wert: {BOX_PLOT_MEDIAN_EVEN}")
    print(f"Das Maximum: {BOX_PLOT_MAX}")
    print(f"Das Minimum: {BOX_PLOT_MIN}")
    print(f"Das Obere Quartil: {BOX_PLOT_UPPER_QUARTILE_EVEN}")
    print(f"Das Untere Quartil: {BOX_PLOT_LOWER_QUARTILE_EVEN}")


def solution_odd():
    print(f"Das Zentral Wert: {BOX_PLOT_MEDIAN_ODD}")
    print(f"Das Maximum: {BOX_PLOT_MAX}")
    print(f"Das Minimum: {BOX_PLOT_MIN}")
    print(f"Das Obere Quartil: {BOX_PLOT_UPPER_QUARTILE_ODD}")
    print(f"Das Untere Quartil: {BOX_PLOT_LOWER_QUARTILE_ODD}")


# Makes a graph under the diagramm
def graph():
    turtle.penup()
    turtle.goto(-300, -100)
    turtle.pendown()
    turtle_Line_shorter()
    num = int_list_sorted[0]
    while(num < int_list_sorted[-1]):
        if num % 5 == 0:
            turtle_Line_shortest()
            turtle.forward(SIZE)
            num = num + 1
        else:
            turtle.forward(SIZE)
            num = num + 1
    turtle_Line_shorter()


print('''
schreib die Zahlen, wenn fertig, schreib cal
check the list, type lis
''')

while(1):
    command = input('> ')
    if command.lower() == 'cal':  
        if len(int_list_sorted) % 2 == 0:
            int_list_sorted.sort
            turtle.penup()
            turtle.goto(-300, 0)
            turtle.pendown()
            solution_even()
            Box_Plot_Maker_even()
            graph()
            turtle.mainloop()
            break
        else:
            int_list_sorted.sort
            turtle.penup()
            turtle.goto(-300, 0)
            turtle.pendown()
            solution_odd()
            Box_Plot_Maker_odd()
            graph()
            turtle.mainloop()
            break
        
    if command.lower() == 'lis':
        print(int_list_sorted)
        print(BOX_PLOT_MAX)

    elif command == float or int:
        int_list_sorted.append(float(command))
        int_list_sorted.sort()
        BOX_PLOT_MIN = item_min(int_list_sorted)
        BOX_PLOT_LOWER_QUARTILE_ODD = lower_quartile_odd(int_list_sorted)
        BOX_PLOT_LOWER_QUARTILE_EVEN = lower_quartile_even(int_list_sorted)
        BOX_PLOT_MEDIAN_ODD = median_odd(int_list_sorted, list_length)
        BOX_PLOT_MEDIAN_EVEN = median_even(int_list_sorted, list_length)
        BOX_PLOT_UPPER_QUARTILE_ODD = upper_quartile_odd(int_list_sorted)
        BOX_PLOT_UPPER_QUARTILE_EVEN = upper_quartile_even(int_list_sorted)
        BOX_PLOT_MAX = item_max(int_list_sorted)
        print("Number has been added")