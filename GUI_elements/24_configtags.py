import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("Texto con múltiples colores")

#text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
#text.pack(expand=True, fill='both')
text = tk.Text(root,
    padx= 10,
    pady= 10,
    font= ("Ink Free", 30),
    width= 20,
    height= 10,
    bg= "light yellow"
    )
text.pack()

# Configurar tags con diferentes colores
text.tag_config('rojo', foreground='red')
text.tag_config('azul', foreground='blue')
text.tag_config('verde', foreground='green')
text.tag_config('negrita', font=('TkDefaultFont', 10, 'bold'))

# Insertar texto con diferentes formatos
text.insert(tk.END, "Este es un texto normal, ")
text.insert(tk.END, "este está en rojo ", 'rojo')
text.insert(tk.END, "y este en azul. ", 'azul')
text.insert(tk.END, "\n\nTambién puedes ", '')
text.insert(tk.END, "combinar ", ('negrita', 'verde'))
text.insert(tk.END, "diferentes formatos.")

root.mainloop()