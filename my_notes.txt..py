# ===============================================
# Tarea: Lectura y Escritura de Archivos en Python
# Archivo: lectura_escritura_archivo.py
# Descripción:
#   Este programa crea un archivo de texto, escribe
#   algunas notas personales, luego las lee y muestra
#   su contenido en consola.
# ===============================================

# ----- ESCRITURA DE ARCHIVO -----
# Se abre (o crea) el archivo 'my_notes.txt' en modo escritura ('w')
# Si el archivo ya existe, se sobrescribe.
with open("my_notes.txt", "w") as file:
    file.write("1. Recordar estudiar para el examen de programación.\n")
    file.write("2. Terminar el proyecto de Python antes del viernes.\n")
    file.write("3. Revisar los apuntes de estructuras de datos.\n")

# ----- LECTURA DE ARCHIVO -----
# Se abre el archivo 'my_notes.txt' en modo lectura ('r')
with open("my_notes.txt", "r") as file:
    # Leer línea por línea con readline()
    print("📘 Contenido del archivo my_notes.txt:\n")
    line = file.readline()
    while line:
        print(line.strip())  # strip() elimina saltos de línea extra
        line = file.readline()

# Al salir del bloque 'with', el archivo también se cierra automáticamente.
print("\n✅ Operaciones completadas correctamente.")
