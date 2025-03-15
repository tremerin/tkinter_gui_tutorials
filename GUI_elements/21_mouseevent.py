import tkinter as tk

window = tk.Tk()

def click(event):
    print(f"mouse coordinates: {event.x}, {event.y}")

#window.bind("<Button-1>", click) #left button
#window.bind("<Button-2>", click) #scroll wheel
#window.bind("<Button-3>", click) #right button
#window.bind("<ButtonRelease>", click)
#window.bind("<Motion>", click) #moving mouse
window.bind("<Enter>", click)
window.bind("<Leave>", click)

window.mainloop()