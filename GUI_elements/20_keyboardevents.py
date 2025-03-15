import tkinter as tk

window = tk.Tk()


def test(event):
    #print(event)
    key_lbl.config(text= event.keysym)
    speed = 2
    #print(window.winfo_x())
    char = event.char
    if char == "d":
        #print("es a!")
        window.geometry(f"+{window.winfo_x() + speed}+{window.winfo_y()}")
    elif char == "a":
        window.geometry(f"+{window.winfo_x() - speed}+{window.winfo_y()}")
    #print(window.winfo_x())

#window.bind("<a>", test)
window.bind("<Key>", test)

key_lbl = tk.Label(window, font=("Helvetica", 100))
key_lbl.pack()


window.mainloop()