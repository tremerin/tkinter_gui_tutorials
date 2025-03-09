import tkinter as tk

window =tk.Tk()
#window.geometry("1000x1000")

photo = tk.PhotoImage(file= "./resources/logo42.png")

label = tk.Label(window, 
                text= "Hello world",
                font= ("Arial", 40, "bold"),
                fg= "#3E464A", #foreground = "red"
                background= "#C0C1C2", #bg = "green"
                relief= "raised", #raised, sunken
                borderwidth= 10,
                padx= 50,
                pady= 10,
                image= photo,
                compound= "bottom") #top, center, left, right

label.pack()
label.pack(fill="both", expand=True)
#label.place(x = 0, y = 10)

window.mainloop()