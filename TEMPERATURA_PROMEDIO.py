# Función para calcular promedios semanales de temperaturas de múltiples ciudades
# La matriz de entrada debe tener la forma:
# temperaturas[ciudad][día][semana]

def calcular_promedios(temperaturas):
    """
    Calcula el promedio semanal de temperatura para cada ciudad.

    Parámetros:
        temperaturas (list): Lista tridimensional donde
            temperaturas[ciudad][día][semana]

    Retorna:
        dict: Un diccionario con promedios por ciudad y semana
    """

    num_ciudades = len(temperaturas)
    num_dias = len(temperaturas[0])
    num_semanas = len(temperaturas[0][0])

    resultados = {}

    for ciudad in range(num_ciudades):
        resultados[f"Ciudad {ciudad}"] = []
        for semana in range(num_semanas):
            suma_semana = 0
            for dia in range(num_dias):
                suma_semana += temperaturas[ciudad][dia][semana]
            promedio_semana = suma_semana / num_dias
            resultados[f"Ciudad {ciudad}"].append(promedio_semana)

    return resultados


# ---------------- PRUEBA DEL CÓDIGO -----------------

temperaturas = [
    [  # Ciudad 0
        [20, 21],  # Lunes
        [22, 23],  # Martes
        [21, 22],  # Miércoles
        [19, 20],  # Jueves
        [20, 21],  # Viernes
        [18, 19],  # Sábado
        [17, 18]  # Domingo
    ],
    [  # Ciudad 1
        [25, 26],
        [24, 25],
        [23, 24],
        [22, 23],
        [21, 22],
        [20, 21],
        [19, 20]
    ]
]

# Llamada a la función
promedios = calcular_promedios(temperaturas)

# Mostrar resultados
for ciudad, valores in promedios.items():
    print(f"\n{ciudad}:")
    for semana, promedio in enumerate(valores, start=1):
        print(f"  Semana {semana}: {promedio:.2f}°C")
