import tkinter as tk

window = tk.Tk()

text = tk.Text(window,
    padx= 10,
    pady= 10,
    font= ("Ink Free", 30),
    width= 20,
    height= 10,
    bg= "light yellow"
    )
text.pack()

def submit():
    
    print(text.get("1.0", tk.END))

submit_btn = tk.Button(window,
    text= "submit",
    command= submit,
    )
submit_btn.pack()

window.mainloop()