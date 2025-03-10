import tkinter as tk

window = tk.Tk()

x = tk.IntVar()

def value():
    print(f"value of scale: {scale.get()}")

scale = tk.Scale(window,
                from_= 0, to= 100,
                length= 200,
                #orient= tk.HORIZONTAL,
                font=("Consolas", 10),
                tickinterval= 20,
                #showvalue= 0,
                resolution= 5,
                troughcolor= "red",
                fg= "blue"
                )
scale.pack()
scale.set(scale["to"]/2)

button = tk.Button(window, text="submit", command= value)
button.pack()

window.mainloop()