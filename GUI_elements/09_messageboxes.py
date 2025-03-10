import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

def click():
    warnings = 0
    #messagebox.showinfo(title= "This is an info message box", message= "This is a message")
    while(warnings < 3):
        messagebox.showwarning(
            title= "WARNING!",
            message= "You are in danger!!"
            )
        warnings += 1

def error():
    messagebox.showerror(title= "ERROR!", message= "Something went wrong :(")

def ask():
    #if messagebox.askokcancel(title= "Ask ok cancel", message= "Do you want to do the thing?"):
    if messagebox.askretrycancel(title= "Ask retry cancel", message= "Do you want retry the thing?"):
        print("You did a thing!")
    else:
        print("You canceced a thing!")
    
click_btn = tk.Button(
    window,
    #command= click,
    command= ask,
    text= "click me!"
    )
click_btn.pack()

error_btn = tk.Button(
    window,
    command= error,
    text= "error"
    )
error_btn.pack()

window.mainloop()