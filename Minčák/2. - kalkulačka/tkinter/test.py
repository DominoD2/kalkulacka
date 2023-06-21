import tkinter as tk

root = tk.Tk()

root.geometry("200x500")
e = tk.Entry(root, width=50, bg="white", fg="black", borderwidth=5)
e.insert(0,"")
e.pack()

def myClick():
    hello = "Ahoj " + e.get()
    myLabel = tk.Label(root, text=hello)
    myLabel.pack()

myButton = tk.Button(root, text="Vlož svoje meno", padx=50, pady=50, command=myClick)
myButton.pack()

root.mainloop()