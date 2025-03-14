import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window,
    height= 500,
    width= 500,
    #border= 10,
    #relief= 'sunken',
    )
canvas.pack()

#line
line1 = canvas.create_line(0, 0, 500, 500, fill= "blue", width= 5)
line2 = canvas.create_line(0, 100, 500, 600, fill= "blue", width= 5)

#rectangle
canvas.create_rectangle(100, 100, 350, 350, fill= "red")

#polygon
points = [0, 0, 250, 500, 400, 100]
canvas.create_polygon(points, fill= "yellow", outline= "black", width= 10)

#arc
points = [50,50, 200, 200]
canvas.create_arc(points, fill= "green", 
    style= tk.CHORD, #PIESLICE, ARC
    start= 180,
    extent = 270,
    )

#oval
canvas.create_oval(230, 230, 270, 270)

window.mainloop()