import tkinter as tk

window = tk.Tk()

def open_file():
    print("open file")
def save_file():
    print("save file")


menu_bar = tk.Menu(window)
window.config(menu= menu_bar)

file_menu = tk.Menu(menu_bar, tearoff= 0)
menu_bar.add_cascade(label= "File", menu= file_menu)
file_menu.add_command(label= "Open", command= open_file)
file_menu.add_command(label= "Save", command= save_file)
file_menu.add_separator()
file_menu.add_command(label= "Exit", command= quit)

edit_menu = tk.Menu(menu_bar, tearoff= 0)
menu_bar.add_cascade(label= "Edit", menu= edit_menu)
edit_menu.add_command(label= "Cut")
edit_menu.add_command(label= "Copy")
edit_menu.add_command(label= "Paste")


window.mainloop()