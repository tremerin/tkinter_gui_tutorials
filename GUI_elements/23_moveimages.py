import tkinter as tk

"""window = tk.Tk()
window.geometry("500x500")
sprite = tk.PhotoImage(file= "./resources/logo42.png").subsample(3, 3)
sprite_lbl = tk.Label(window, image= sprite)
window.update_idletasks()
speed = 5
print(sprite.width())
sprite_lbl.place(x= window.winfo_width() / 2 - sprite.width() / 2, 
                 y= window.winfo_height() / 2 - sprite.height() / 2)


def move(event):
    char = event.char
    x_speed = 0
    y_speed = 0
    if char == "a": x_speed = -speed
    elif char == "d": x_speed = speed
    elif char == "w": y_speed = -speed
    elif char == "s": y_speed = speed
    sprite_lbl.place(x= sprite_lbl.winfo_x() + x_speed,
                    y= sprite_lbl.winfo_y() + y_speed)

window.bind("<Key>", move)

window.mainloop()"""

window = tk.Tk()


canvas = tk.Canvas(window, width= 500, height= 500)
canvas.pack()

img = image= tk.PhotoImage(file= "./resources/logo_python.png")
sprite = canvas.create_image(10, 10, image = img, anchor= tk.NW)

speed = 5
def move(event):
    char = event.char
    x_speed = 0
    y_speed = 0
    if char == "a": x_speed = -speed
    elif char == "d": x_speed = speed
    elif char == "w": y_speed = -speed
    elif char == "s": y_speed = speed
    canvas.move(sprite, x_speed, y_speed)

window.bind("<Key>", move)


window.mainloop()