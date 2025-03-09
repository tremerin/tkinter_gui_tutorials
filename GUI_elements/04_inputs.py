import tkinter as tk

window = tk.Tk()

def submit():
    username = entry.get()
    print(username)

def delete():
    entry.delete(0, tk.END)

def backspace():
    entry.delete(len(entry.get())-1, tk.END)

submit_btn = tk.Button(window,
                       text= "submit",
                       command= submit,
                       font= ("Arial", 25),
                       )
submit_btn.pack(side= "right")

delete_btn = tk.Button(window,
                       text= "delete",
                       command= delete,
                       font= ("Arial", 25),
                       )
delete_btn.pack(side= "right")

backspace_btn = tk.Button(window,
                       text= "backspace",
                       command= backspace,
                       font= ("Arial", 25),
                       )
backspace_btn.pack(side= "right")

entry = tk.Entry()
entry.config(font=("Ink Free", 30),
            bg= "red",
            fg= "white",
            bd= 10)
entry.insert(0, "here!")
entry.config(state= "normal")
#entry.config(width= 10)
#entry.config(show= "*")
entry.pack()

window.mainloop()