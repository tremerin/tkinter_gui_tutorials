import tkinter as tk
import tkinter.ttk as ttk
import time

window = tk.Tk()

def start():
    for i in range(10):
        bar["value"] += 10
        window.update_idletasks()  # Refresca la ventana para mostrar cambios
        time.sleep(0.2)
    bar["value"] = 0 

bar = ttk.Progressbar(window, length=200, orient="horizontal", mode="determinate")
bar.pack(pady=10, padx=10)

download_btn = tk.Button(window, text="Download", command=start)
download_btn.pack(pady=10)

window.mainloop()