import tkinter as tk
from tkinter import colorchooser

window = tk.Tk()

def color():
    choosen = colorchooser.askcolor()
    window.config(bg= choosen[1])

color_btn = tk.Button(window,
            text= "Choose color",
            command= color,
            )
color_btn.pack()

window.mainloop()