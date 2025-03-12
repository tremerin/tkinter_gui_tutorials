import tkinter as tk

window = tk.Tk()

frame = tk.Frame(window, bg= "pink", bd= 5, relief= "sunken")
frame.pack()

tk.Button(frame, text= "W", font=("Consolas", 25), width= 3).pack(side= "top")
tk.Button(frame, text= "A", font=("Consolas", 25), width= 3).pack(side= "left")
tk.Button(frame, text= "S", font=("Consolas", 25), width= 3).pack(side= "left")
tk.Button(frame, text= "D", font=("Consolas", 25), width= 3).pack(side= "left")

window.mainloop()