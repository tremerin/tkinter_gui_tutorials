import tkinter as tk
import subprocess


def execute():
    print("Executing")
    #subprocess.run(["python", "program.py", "hola", "holita"])
    process = subprocess.Popen(["python", "program.py", "arg1"], stdout=subprocess.PIPE, text=True)
    #print(process)
    print("--- End ---")

window = tk.Tk()

#process = ""
exe_btn = tk.Button(window, text="Execute", command= execute)
exe_btn.pack()

"""print(type(process))
for line in process.stdout:
    print(type(line))
    print(line)"""

window.mainloop()