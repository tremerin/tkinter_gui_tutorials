import tkinter as tk
from tkinter import scrolledtext
import re

def resaltar_palabras():
    # Palabras clave y sus formatos
    palabras_clave = {
        'import': ('azul', 'negrita'),
        'def': ('rojo', 'negrita'),
        'class': ('verde', 'negrita'),
        'self': ('magenta',)
    }
    
    # Obtener todo el texto
    contenido = text.get(1.0, tk.END)
    
    # Borrar y volver a insertar con formatos
    text.delete(1.0, tk.END)
    
    # Dividir el texto usando expresiones regulares
    patron = re.compile(r'(\W|\s)(' + '|'.join(re.escape(p) for p in palabras_clave.keys()) + r')(\W|\s)')
    partes = patron.split(contenido)
    
    for i in range(len(partes)):
        if i % 4 == 2:  # Las palabras clave están en las posiciones 2, 6, 10...
            palabra = partes[i]
            if palabra in palabras_clave:
                text.insert(tk.END, palabra, palabras_clave[palabra])
            else:
                text.insert(tk.END, palabra)
        else:
            text.insert(tk.END, partes[i] if partes[i] else '')

root = tk.Tk()
root.title("Resaltado de sintaxis")

text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
text.pack(expand=True, fill='both')

# Configurar tags
text.tag_config('rojo', foreground='red')
text.tag_config('azul', foreground='blue')
text.tag_config('verde', foreground='green')
text.tag_config('magenta', foreground='magenta')
text.tag_config('negrita', font=('TkDefaultFont', 10, 'bold'))

# Insertar texto de ejemplo
text.insert(tk.END, """import tkinter as tk

class MiAplicacion:
    def __init__(self, root):
        self.root = root
        self.crear_interfaz()
    
    def crear_interfaz(self):
        pass
""")

# Botón para resaltar
btn = tk.Button(root, text="Resaltar palabras clave", command=resaltar_palabras)
btn.pack(pady=5)

root.mainloop()