import turtle
from functions_calculation import *

with open('input.txt', encoding='utf-8') as f:
    CONTENT = f.read()
    f.close()

def get_int_list(array: str):
    string_array = array.split(" ")
    int_array = [int(n) for n in string_array]
    return int_array

int_list = get_int_list(CONTENT)
int_list_sorted = sorted(int_list)
list_length = len(int_list)
SIZE = 10

BOX_PLOT_MIN = item_min(int_list_sorted)
BOX_PLOT_LOWER_QUARTILE_ODD = lower_quartile_odd(int_list_sorted)
BOX_PLOT_LOWER_QUARTILE_EVEN = lower_quartile_even(int_list_sorted)
BOX_PLOT_MEDIAN_ODD = median_odd(int_list_sorted, list_length)
BOX_PLOT_MEDIAN_EVEN = median_even(int_list_sorted, list_length)
BOX_PLOT_UPPER_QUARTILE_ODD = upper_quartile_odd(int_list_sorted)
BOX_PLOT_UPPER_QUARTILE_EVEN = upper_quartile_even(int_list_sorted)
BOX_PLOT_MAX = item_max(int_list_sorted)


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

# Hier macht es die box für den unteres Quartil, wenn die Liste hat gerade Anzahl Elemente
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

# Hier macht es die box für den unteres Quartil, wenn die Liste hat ungerade Anzahl # Elemente
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

# Hier macht es die box für den oberes Quartil, wenn die Liste hat gerade Anzahl Elemente
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

# Hier macht es die box für den oberes Quartil, wenn die Liste hat ungerade Anzahl # Elemente
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

# alle Unterprogramme gehen in diese unterprogramm, wo zuständig für bauen des Box-plot, # wenn die Liste hat gerade Anzahl Elemente
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

# alle Unterprogramme gehen in diese unterprogramm, wo zuständig für bauen des Box-plot, # wenn die Liste hat ungerade Anzahl Elemente
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

# gibt dir die Ergebnisse
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
# Es fangt am gleichen Ort aber tiefer und mach eine Linie jede 5 mal
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
''')

while(1):
    command = input('> ')
    if command.lower() == 'cal':
        if (len(int_list_sorted) % 2) == 0:
            int_list_sorted.sort
            turtle.penup()
            turtle.goto(-300, 0)
            turtle.pendown()
            Box_Plot_Maker_even()
            graph()
            turtle.mainloop()
            break
        else:
            int_list_sorted.sort
            turtle.penup()
            turtle.goto(-300, 0)
            turtle.pendown()
            Box_Plot_Maker_odd()
            graph()
            turtle.mainloop()
            break
    else:
        int_list.append(int(command))
        print('habe dazu gegeben')