import tkinter as tk

window = tk.Tk()

def new_window():
    new = tk.Tk()

tk.Button(text= "New window", command= new_window).pack()

window.mainloop()