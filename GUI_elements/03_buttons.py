import tkinter as tk

window = tk.Tk()
window.geometry("620x420")

count:int = 0
def click():
    global count 
    count += 1
    label.config(text= count)
    print(count)

#button config
button = tk.Button(window, text= "Click me!")
button.config(command= click)
button.config(font= ("Ink Free", 50, "bold"))
button.config(bg= "#ff6200")
button.config(fg= "#f0ff14")
button.config(activebackground= "#FF0000")
button.config(activeforeground= "#f0ff14")

image = tk.PhotoImage(file= "./resources/hand-emoji.png").subsample(3, 3)

button.config(image= image)
button.config(compound= "left")
button.config(relief= "sunken")
button.config(bd= 10)
button.config(pady= 20)
button.config(padx= 20) 
button.config(state= "active") # or disabled

#button.pack()
button.place(x = 50, y = 80)

#label config
label = tk.Label(window, text= count)
label.config(font= ("Arial", 40))
label.pack()


window.mainloop()