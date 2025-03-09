import tkinter as tk

window = tk.Tk()

def display():
    if x.get() == 1 and y.get() == 1:
        print("I like Python and Java")
    elif x.get() == 1 and y.get() == 0:
        print("I like Python")
    elif x.get() == 0 and y.get() == 1:
        print("I like Java")
    else:
        print("I don´t like either")

#pytho checkbox
x = tk.IntVar()
checkbox = tk.Checkbutton(
    window, text= "Python",
    variable= x,
    onvalue= 1,
    offvalue= 0,
    command= display        
    )
checkbox.pack()
checkbox.config(font=("Arial", 20))
checkbox.config(fg= "#0000ff")
checkbox.config(bg= "#000000")
checkbox.config(activeforeground= "#0000ff")
checkbox.config(activebackground= "#000000")

icon_python = tk.PhotoImage(file= "./resources/logo_python.png")
checkbox.config(image= icon_python)
checkbox.config(compound= "left")
checkbox.config(padx= 25, pady= 10,
                width= 250, height= 50)
checkbox.config(anchor="w")

#java checkbox
y = tk.IntVar()
checkbox2 = tk.Checkbutton(
    window, text= "Java",
    variable= y,
    onvalue= 1,
    offvalue= 0,
    command= display        
    )
checkbox2.pack()
checkbox2.config(font=("Arial", 20))
checkbox2.config(fg= "#0000ff")
checkbox2.config(bg= "#000000")
checkbox2.config(activeforeground= "#0000ff")
checkbox2.config(activebackground= "#000000")

icon_java = tk.PhotoImage(file= "./resources/logo_java.png")
checkbox2.config(image= icon_java)
checkbox2.config(compound= "left")
checkbox2.config(padx= 25, pady= 10,
                width= 250, height= 50)
checkbox2.config(anchor="w")

window.mainloop()