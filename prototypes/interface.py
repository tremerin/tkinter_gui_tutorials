import tkinter as tk
from tkinter import scrolledtext
import subprocess
import sys
import re

def execute():
    #print("ft execute")
    process = subprocess.Popen(arguments, stdout=subprocess.PIPE, text=True)
    out = ""
    for line in process.stdout:
        out = out + line 
    original_text = out
    text.insert(tk.END, original_text)
    #print(original_text)


window = tk.Tk()

name = "python"
if sys.platform == "linux":
    name = "python3"

original_text = tk.StringVar()
argv1 = f"\033[41mtexto\033[0m"
argv2 = f"otro \033[41mtexto2\033[0m mas"
arguments = [name, "program.py", argv1, argv2, "arg3"]
exe_btn = tk.Button(window, text="Execute", command= execute)
exe_btn.pack()

original = f"\033[41mtexto\033[0m test 33"
#regex = r"\d+"
regex = r"\033\[41m"

result = re.sub(regex, "", original)
print(original)
print(result)


text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20)
text.pack(expand=True, fill='both')


# Configurar tags con diferentes colores
text.tag_config('rojo', foreground='red')
text.tag_config('azul', foreground='blue')
text.tag_config('verde', foreground='green')
text.tag_config('negrita', font=('TkDefaultFont', 10, 'bold'))


window.mainloop()