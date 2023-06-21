import tkinter as tk
from PIL import ImageTk, Image

bmi = 0

def výpočet_bmi():
    global bmi, nieco, img
    výška = float(výška_entry.get()) / 100
    váha = float(váha_entry.get())
    bmi = váha / (výška ** 2)
    bmi = float(bmi)
    výsledok_label.config(text="Tvoje BMI je {:.1f}".format(bmi))
    if bmi > 0.0 and bmi < 20.0:
        img = ImageTk.PhotoImage(Image.open("anorexia.jpg"))
        nieco = tk.Label(root, image=img)
        nieco.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    elif bmi >= 20.0 and bmi < 25.0:
        img = ImageTk.PhotoImage(Image.open("normal.png"))
        nieco = tk.Label(root, image=img)
        nieco.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    elif bmi >= 25.0:
        img = ImageTk.PhotoImage(Image.open("obezita.jpg"))
        nieco = tk.Label(root, image=img)
        nieco.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


root = tk.Tk()
root.title("BMI kalkulačka")

výška_label = tk.Label(root, text="Výška (cm):", borderwidth=3)
výška_label.grid(row=0, column=0, padx=5, pady=5)

výška_entry = tk.Entry(root)
výška_entry.grid(row=0, column=1, padx=5, pady=5)

váha_label = tk.Label(root, text="Váha (kg):", borderwidth=3)
váha_label.grid(row=1, column=0, padx=5, pady=5)

váha_entry = tk.Entry(root)
váha_entry.grid(row=1, column=1, padx=5, pady=5)

výpočet_button = tk.Button(root, text="Vypočítaj BMI", command=výpočet_bmi, borderwidth=3)
výpočet_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

výsledok_label = tk.Label(root, text="")
výsledok_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()