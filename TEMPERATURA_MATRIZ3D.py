# Temperaturas: ciudades x días x semanas
# matriz3D[ciudad][día][semana]

temperaturas = [
    [   # Ciudad 0
        [20, 21],  # Lunes
        [22, 23],  # Martes
        [21, 22],  # Miércoles
        [19, 20],  # Jueves
        [20, 21],  # Viernes
        [18, 19],  # Sábado
        [17, 18]   # Domingo
    ],
    [   # Ciudad 1
        [25, 26],
        [24, 25],
        [23, 24],
        [22, 23],
        [21, 22],
        [20, 21],
        [19, 20]
    ]
]
num_ciudades = len(temperaturas)
num_dias = len(temperaturas[0])
num_semanas = len(temperaturas[0][0])

for ciudad in range(num_ciudades):
    print(f"\nPromedios para Ciudad {ciudad}:")
    for semana in range(num_semanas):
        suma_semana = 0
        for dia in range(num_dias):
            suma_semana += temperaturas[ciudad][dia][semana]
        promedio_semana = suma_semana / num_dias
        print(f"  Semana {semana + 1}: {promedio_semana:.2f}°C")