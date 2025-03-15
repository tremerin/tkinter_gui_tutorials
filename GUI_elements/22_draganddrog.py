import tkinter as tk

window = tk.Tk()
window.geometry("400x400")

"""def drag_start(event):
    print("click")
    red_lbl.start_x = event.x
    red_lbl.start_y = event.y

def drag_motion(event):
    x = red_lbl.winfo_x() - red_lbl.start_x + event.x
    y = red_lbl.winfo_y() - red_lbl.start_y + event.y
    red_lbl.place(x= x, y= y)"""


def drag_start(event):
    widget = event.widget
    widget.start_x = event.x
    widget.start_y = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.start_x + event.x
    y = widget.winfo_y() - widget.start_y + event.y
    widget.place(x= x, y= y)

red_lbl = tk.Label(bg= "red", width= 10, height= 5)
red_lbl.place(x= 0, y= 0)
red_lbl.bind("<Button-1>", drag_start)
red_lbl.bind("<B1-Motion>", drag_motion)

blue_lbl = tk.Label(bg= "blue", width= 10, height= 5)
blue_lbl.place(x= 100, y= 200)
blue_lbl.bind("<Button-1>", drag_start)
blue_lbl.bind("<B1-Motion>", drag_motion)

window.mainloop()