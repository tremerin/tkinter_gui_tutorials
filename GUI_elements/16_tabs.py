import tkinter as tk
from tkinter import ttk

window = tk.Tk()

notebook =  ttk.Notebook(window)

tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)

notebook.add(tab1, text= "Tab 1")
notebook.add(tab2, text= "Tab 2")
notebook.pack(expand=True, fill= "both")

tk.Label(tab1, text= "Tab 1", width= 50, height= 25).pack()
tk.Label(tab2, text= "Tab 2", width= 50, height= 25).pack()

window.mainloop()