import turtle
pero = turtle.Turtle()
tabula = turtle.Screen()

pero.width(3)
pero.speed(0.001)

x = 10

def rekurzia(i):
    global x
    x = x + 5
    pero.forward(x)
    pero.left(60)
    if i == 1:
        return i
    else:
        return rekurzia(i-1)
rekurzia(31)

tabula.mainloop()