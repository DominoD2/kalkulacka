import tkinter as tk

root = tk.Tk()
root.title("Kalkulačka")

e = tk.Entry(root, width=40, borderwidth=7)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add(num):
    current = e.get()
    e.delete(0,"end")
    e.insert(0, str(current) + str(num))
    return

def button_clear():
    e.delete(0, "end")

def button_ad():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, "end")
    global operator
    operator = "+"

def button_substract():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, "end")
    global operator
    operator = "-"

def button_multiply():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, "end")
    global operator
    operator = "*"

def button_divide():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, "end")
    global operator
    operator = "/"


def button_equal():
    second_number = e.get()
    s_num = int(second_number)
    e.delete(0, "end")
    if operator == "+":
        e.insert(0, f_num + s_num)
    elif operator == "-":
        e.insert(0, f_num - s_num)
    elif operator == "*":
        e.insert(0, f_num * s_num)
    elif operator == "/":
        e.insert(0, f_num / s_num)


button_1 = tk.Button(root, text="1", padx=50, pady=20, command=lambda: button_add(1), borderwidth=5)
button_2 = tk.Button(root, text="2", padx=50, pady=20, command=lambda: button_add(2), borderwidth=5)
button_3 = tk.Button(root, text="3", padx=52, pady=20, command=lambda: button_add(3), borderwidth=5)
button_4 = tk.Button(root, text="4", padx=50, pady=20, command=lambda: button_add(4), borderwidth=5)
button_5 = tk.Button(root, text="5", padx=50, pady=20, command=lambda: button_add(5), borderwidth=5)
button_6 = tk.Button(root, text="6", padx=52, pady=20, command=lambda: button_add(6), borderwidth=5)
button_7 = tk.Button(root, text="7", padx=50, pady=20, command=lambda: button_add(7), borderwidth=5)
button_8 = tk.Button(root, text="8", padx=50, pady=20, command=lambda: button_add(8), borderwidth=5)
button_9 = tk.Button(root, text="9", padx=52, pady=20, command=lambda: button_add(9), borderwidth=5)
button_0 = tk.Button(root, text="0", padx=50, pady=20, command=lambda: button_add(0), borderwidth=5)
button_ad = tk.Button(root, text="+", padx=49, pady=20, command=button_ad, borderwidth=5)
button_equal = tk.Button(root, text="=", padx=111, pady=20, command=button_equal, borderwidth=5)
button_clear = tk.Button(root, text="Clear", padx=102, pady=20, command=button_clear, borderwidth=5)
button_substract = tk.Button(root, text="-", padx=50, pady=20, command=button_substract, borderwidth=5)
button_multiply = tk.Button(root, text="*", padx=50, pady=20, command=button_multiply, borderwidth=5)
button_divide = tk.Button(root, text="/", padx=52, pady=20, command=button_divide, borderwidth=5)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_ad.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_substract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)



root.mainloop()