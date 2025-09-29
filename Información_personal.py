# Diccionario inicial
informacion_personal = {
    "Nombre": "Jenny Manzano",
    "Edad": 18,
    "Ciudad": "Quito",
    "Profesion": "Ingeniero"
}

# Modificar ciudad
informacion_personal["Ciudad"] = "Cuyabeno"

# Actualizar profesion
informacion_personal["Profesion"] = "Estudiante"

# Verificar existencia de "telefono"
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "0968089605"

# Eliminar "edad" sin error
informacion_personal.pop("Edad", None)

# Imprimir diccionario final
print("Diccionario final:")
print(informacion_personal)
