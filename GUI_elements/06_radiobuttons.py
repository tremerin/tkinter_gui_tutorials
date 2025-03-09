import tkinter as tk

window = tk.Tk()

languages = [("C", tk.PhotoImage(file="./resources/logo_c.png")),
             ("C++", tk.PhotoImage(file="./resources/logo_c++.png")), 
             ("Python", tk.PhotoImage(file="./resources/logo_python.png"))
            ]

x = tk.IntVar()
x.set(-1)

def my_value():
    print(f"selected: {languages[x.get()][0]}")
          
for i in range(len(languages)):
    radiobutton = tk.Radiobutton(window, 
        text= languages[i][0],
        variable= x,
        value= i,
        command= my_value,
        padx= 25, 
        pady= 5,
        #width= 150, 
        #height= 50,
        #anchor= "w"
        font= ("Impact", 16),
        image= languages[i][1],
        compound= "left",
        #indicatoron=0,
        )
    radiobutton.pack(anchor= tk.W)
window.mainloop()