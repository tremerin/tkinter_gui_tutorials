"""import tkinter as tk

window = tk.Tk()
#window2 = tk.Tk()

new_win = tk.Variable()

def new_window():
    #new = tk.Tk()
    global new_win
    new_win = tk.Toplevel()

def clear_window():
    if new_win:
        new_win.destroy()

tk.Button(text= "New window", command= new_window).pack()
tk.Button(text= "Clear window", command= clear_window).pack()

#print(window.winfo_exists)
window.mainloop()
#window2.mainloop()"""

import tkinter as tk

def abrir_ventana():
    global ventana_secundaria  # Usamos una variable global para la ventana secundaria
    
    if ventana_secundaria is None: #or not ventana_secundaria.winfo_exists():
        ventana_secundaria = tk.Toplevel(root)  # Crear la ventana secundaria
        ventana_secundaria.title("Ventana Secundaria")

        # Manejar el evento de cierre para resetear la variable
        ventana_secundaria.protocol("WM_DELETE_WINDOW", cerrar_ventana)
    else:
        ventana_secundaria.lift()  # Si ya está abierta, traerla al frente

def cerrar_ventana():
    global ventana_secundaria
    ventana_secundaria.destroy()  # Cerrar la ventana
    ventana_secundaria = None  # Resetear la variable para permitir abrir otra

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana Principal")

# Variable global para almacenar la ventana secundaria
ventana_secundaria = None

# Botón para abrir la ventana secundaria
boton = tk.Button(root, text="Abrir Ventana", command=abrir_ventana)
boton.pack(pady=10)

root.mainloop()

