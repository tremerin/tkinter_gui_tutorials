import tkinter as tk
import subprocess


def execute():
    print("Executing")
    #subprocess.run(["python", "program.py", "hola", "holita"])
    #args = ["python", "program.py", "arg1", "arg2", "arg3"]
    process = subprocess.Popen(arguments, stdout=subprocess.PIPE, text=True)
    out = ""
    for line in process.stdout:
        out = out + line 
    #print(out)
    lbl_text.config(text=out)
    print("--- End ---")

window = tk.Tk()

arguments = tk.StringVar()
arguments = ["python", "program.py", "arg1", "arg2", "arg3"]
exe_btn = tk.Button(window, text="Execute", command= execute)
exe_btn.pack()

lbl_text = tk.Label(text= f"\033[41m texto \033[0m")
lbl_text.pack()


window.mainloop()