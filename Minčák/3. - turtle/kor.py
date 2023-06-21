import turtle
pero = turtle.Turtle()
tabula = turtle.Screen()

pero.width(3)
pero.speed(0.001)
def trojuholnik(dlzka):
    for i in range(3):
            pero.forward(dlzka)
            pero.left(120)

def rad_trojuholnikov(pocet, dlzka):
    for i in range(pocet):
        trojuholnik(dlzka)
        pero.forward(dlzka)
    pero.forward(-dlzka * pocet)

def pyramida(pocet, dlzka):
    for i in range(pocet, 0, -1):
         rad_trojuholnikov(i, dlzka)
         pero.left(60)
         pero.forward(dlzka)
         pero.right(60)

pyramida(5, 30)
tabula.mainloop()