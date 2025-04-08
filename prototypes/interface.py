import tkinter as tk
import subprocess
import sys
import re

def execute():
    print("ft execute")
    #subprocess.run(["python", "program.py", "hola", "holita"])
    #args = ["python", "program.py", "arg1", "arg2", "arg3"]
    process = subprocess.Popen(arguments, stdout=subprocess.PIPE, text=True)
    out = ""
    for line in process.stdout:
        out = out + line 
    #print(out)
    lbl_text.config(text=out)
    #print("--- End ---")

window = tk.Tk()

#arguments = tk.StringVar()
name = "python"
if sys.platform == "linux":
    name = "python3"
arguments = [name, "program.py", "arg1", "arg2", "arg3"]
exe_btn = tk.Button(window, text="Execute", command= execute)
exe_btn.pack()

original = f"\033[41mtexto\033[0m"
#regex = r"\\\d+\[\d+m ?"
regex = r"\d+"
#span = re.match(regex, original)
#print(span)
result = re.sub(regex, "", original)
print(f"result: {result}")

lbl_text = tk.Label(text= result)
lbl_text.pack()


window.mainloop()