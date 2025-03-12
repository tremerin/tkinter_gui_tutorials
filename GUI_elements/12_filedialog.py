import tkinter as tk
from tkinter import filedialog

window = tk.Tk()

def open_file():
    file_path = filedialog.askopenfilename(
        initialdir= ".",
        title= "open file?",
        filetypes= (("text files", "*.txt"), ("all files", "*.*"))
        )
    if file_path:
        file = open(file_path, "r")
        new_text = file.read()
        print(new_text)
        text_box.insert("1.0", new_text)
        file.close()

def save_file():
    file = filedialog.asksaveasfile(
        initialdir= ".",
        defaultextension= ".txt",
        filetypes= [("Text file", "*.txt")]
        )
    file_text = str(text_box.get(1.0, tk.END))
    file.write(file_text)
    file.close()        

open_btn = tk.Button(window,
    text= "Open file",
    command= open_file,
    )
open_btn.pack()

save_btn = tk.Button(window, text= "Save file", command= save_file)
save_btn.pack()

text_box = tk.Text(window,
    padx= 10,
    pady= 10,
    font= ("Ink Free", 20),
    width= 20,
    height= 10,
    bg= "light yellow"
    )
text_box.pack()

window.mainloop()