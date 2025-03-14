import tkinter as tk

window = tk.Tk()


def test(event):
    print(event.keysym)
    key_lbl.config(text= event.keysym)
    #window.geometry("+10+0")

#window.bind("<a>", test)
window.bind("<Key>", test)

key_lbl = tk.Label(window, font=("Helvetica", 100))
key_lbl.pack()


window.mainloop()