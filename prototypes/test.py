import subprocess 

# Pasar argumentos a 'programa1.py'
process = subprocess.Popen(["python", "program.py", "arg1", "arg22", "arg3"], stdout=subprocess.PIPE, text=True)

# Leer la salida de programa1.py
for line in process.stdout:
    print(f"Received: {line}", end="")
