import turtle

# diese Zahlen können sie in die eingeben, damit es nicht mühsam mit dem programm es zu # machen -> 32,32,33,32,42,34,45,53,30,44,37,25

# Wo alles anfangt, die Liste mit allen Daten, um eine Box-Plot zu bauen
List = [32,32,33,32,42,34,45,53,30,44,37,25,23]

# Wie gross in Länge die Box-Plot gebaut wird
Size = 10

# Die Spannweite zu berechnen (unnötig, ist wichtig, wenn das rechnen des Box-Plot Länge)
def SW():
    global SpannWeite
    List.sort()
    SpannWeite = List[-1] - List[0]

# den Zentralwert finden, wenn die Liste hat gerade Anzahl Elemente
def ZW_even():
    global ZentralWert_even
    List.sort()
    Items = (len(List))
    num1 = Items//2-1
    num2 = Items//2
    ZentralWert_even = (List[num1] + List[num2]) / 2

# den Zentralwert finden, wenn die Liste hat ungerade Anzahl Elemente
def ZW_odd():
    global ZentralWert_odd
    List.sort()
    Items = (len(List))
    num2 = Items//2
    ZentralWert_odd = List[num2]

# Die grösste Zahl in der Liste zu finden
def MAX():
    global maximum
    maximum = (max(List))

# Die kleinste Zahl in der Liste zu finden
def MIN():
    global minimum
    minimum = (min(List))

# Den Oberes Quartil zu finden, wenn die Liste hat gerade Anzahl Elemente
def OQuart_even():
    global ObererQuartal_even
    List.sort()
    Half_List = []
    Half_List.extend(List[len(List)//2:])
    Items = len(Half_List)
    num1 = Items // 2 - 1
    num2 = Items // 2
    ObererQuartal_even = float((Half_List[num1] + Half_List[num2]) / 2)

# Den Oberes Quartil zu finden, wenn die Liste hat ungerade Anzahl Elemente
def OQuart_odd():
    global ObererQuartal_odd
    List.sort()
    Half_List = []
    Half_List.extend(List[len(List)//2+1:])
    Items = len(Half_List)
    num1 = Items // 2 - 1
    num2 = Items // 2
    ObererQuartal_odd = float((Half_List[num1] + Half_List[num2]) / 2)

# Den unteres Quartil zu finden, wenn die Liste hat gerade Anzahl Elemente
def UQuart_even():
    global UntererQuartal_even
    List.sort()
    Half_List = []
    Half_List.extend(List[:len(List)//2])
    Items = len(Half_List)
    num1 = Items // 2 - 1
    num2 = Items // 2
    UntererQuartal_even = float((Half_List[num1] + Half_List[num2]) / 2)

# Den unteres Quartil zu finden, wenn die Liste hat ungerade Anzahl Elemente
def UQuart_odd():
    global UntererQuartal_odd
    List.sort()
    Half_List = []
    Half_List.extend(List[:len(List)//2+1])
    Items = len(Half_List)
    num1 = Items // 2 - 1
    num2 = Items // 2
    UntererQuartal_odd = float((Half_List[num1] + Half_List[num2]) / 2)

# alle unterprogramme öffnen um die Daten zu bekommen (sehr wichtig!)
def calculation():
    SW()
    ZW_even()
    ZW_odd()
    MAX()
    MIN()
    OQuart_even()
    UQuart_even()
    OQuart_odd()
    UQuart_odd()

# Hier kommt das Zeichnen des Box-Plots
# dieses Unterprogramm macht die Linie aufrecht am anfang und ende des Box-Plots
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
    turtle.forward((ZentralWert_even - UntererQuartal_even) * Size)
    turtle.left(90)
    turtle.forward(40*2)
    turtle.left(90)
    turtle.forward((ZentralWert_even - UntererQuartal_even) * Size)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)

# Hier macht es die box für den unteres Quartil, wenn die Liste hat ungerade Anzahl # Elemente
def Box1_odd():
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward((ZentralWert_odd - UntererQuartal_odd) * Size)
    turtle.left(90)
    turtle.forward(40*2)
    turtle.left(90)
    turtle.forward((ZentralWert_odd - UntererQuartal_odd) * Size)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)

# Hier macht es die box für den oberes Quartil, wenn die Liste hat gerade Anzahl Elemente
def Box2_even():
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward((ObererQuartal_even - ZentralWert_even) * Size)
    turtle.right(90)
    turtle.forward(40*2)
    turtle.right(90)
    turtle.forward((ObererQuartal_even - ZentralWert_even) * Size)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)

# Hier macht es die box für den oberes Quartil, wenn die Liste hat ungerade Anzahl # Elemente
def Box2_odd():
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward((ObererQuartal_odd - ZentralWert_odd) * Size)
    turtle.right(90)
    turtle.forward(40*2)
    turtle.right(90)
    turtle.forward((ObererQuartal_odd - ZentralWert_odd) * Size)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)

# alle Unterprogramme gehen in diese unterprogramm, wo zuständig für bauen des Box-plot, # wenn die Liste hat gerade Anzahl Elemente
def Box_Plot_Maker_even():
    calculation()
    solution_even()
    Turtle_Line_short()
    turtle.forward((UntererQuartal_even - minimum)*Size)
    Box1_even()
    turtle.penup()
    turtle.forward((ZentralWert_even - UntererQuartal_even) * Size)
    turtle.pendown()
    Box2_even()
    turtle.penup()
    turtle.forward((ObererQuartal_even - ZentralWert_even) * Size)
    turtle.pendown()
    turtle.forward((maximum - ObererQuartal_even) * Size)
    Turtle_Line_short()

# alle Unterprogramme gehen in diese unterprogramm, wo zuständig für bauen des Box-plot, # wenn die Liste hat ungerade Anzahl Elemente
def Box_Plot_Maker_odd():
    calculation()
    solution_odd()
    Turtle_Line_short()
    turtle.forward((UntererQuartal_odd - minimum)*Size)
    Box1_odd()
    turtle.penup()
    turtle.forward((ZentralWert_odd - UntererQuartal_odd) * Size)
    turtle.pendown()
    Box2_odd()
    turtle.penup()
    turtle.forward((ObererQuartal_odd - ZentralWert_odd) * Size)
    turtle.pendown()
    turtle.forward((maximum - ObererQuartal_odd) * Size)
    Turtle_Line_short()

# gibt dir die Ergebnisse
def solution_even():
    print(f"Das Zentral Wert: {ZentralWert_even}")
    print(f"Das Maximum: {maximum}")
    print(f"Das Minimum: {minimum}")
    print(f"Das Obere Quartil: {ObererQuartal_even}")
    print(f"Das Untere Quartil: {UntererQuartal_even}")

def solution_odd():
    print(f"Das Zentral Wert: {ZentralWert_odd}")
    print(f"Das Maximum: {maximum}")
    print(f"Das Minimum: {minimum}")
    print(f"Das Obere Quartil: {ObererQuartal_odd}")
    print(f"Das Untere Quartil: {UntererQuartal_odd}")
# Es fangt am gleichen Ort aber tiefer und mach eine Linie jede 5 mal
def graph():
    List.sort()
    turtle.penup()
    turtle.goto(-300, -100)
    turtle.pendown()
    turtle_Line_shorter()
    num = List[0]
    while(num < List[-1]):
        if num % 5 == 0:
            turtle_Line_shortest()
            turtle.forward(Size)
            num = num + 1
        else:
            turtle.forward(Size)
            num = num + 1
    turtle_Line_shorter()

# die erklärung gedruckt
print('''
schreib die Zahlen, wenn fertig, schreib cal
''')

# geht in einem loop
while(1):

# die Person schreibt entweder die nummer für die Liste oder cal, damit das bauen starten
    command = input('> ')

# wenn es cal ist
    if command.lower() == 'cal':

# Es schaut, ob in der Liste gerade oder ungerade anzahl Elemente hat und macht die Boxplot
        if (len(List) % 2) == 0:

# wenn Anzahl gerade
            turtle.penup()
            turtle.goto(-300, 0)
            turtle.pendown()
            Box_Plot_Maker_even()
            graph()
            turtle.mainloop()
            break
        else:

# wenn Anzahl ungerade
            turtle.penup()
            turtle.goto(-300, 0)
            turtle.pendown()
            Box_Plot_Maker_odd()
            graph()
            turtle.mainloop()
            break

# wenn es nicht cal, gibt es die Zahl zu Liste dazu (wichtig, muss zum intiger gewechselt werden!)
    else:
        List.append(int(command))
        print('habe dazu gegeben')