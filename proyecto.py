import random

print("------------------- Asignacion de tareas-------------------")

# Asignacion de tareas.
tareas = [
    {
        "nombre": "Tarea 1",
        "descripcion": "Realizar una serie de actividades diarias a partir de esta lista",
        "instrucciones": [
            "Levantarse",
            "Irse a cepillar los dientes",
            "Tender la cama",
            "Irse a bañar",
            "Ponerse la ropa (opciones: Op1: Camisa, Traje de paño, corbata, zapatos, cinturón, reloj, pantalón, boxers, Op2: Chaqueta, Camisa, Jean, Boxers, medias, Tenis)",
            "Desayunarse",
            "Salir de la casa",
            "Coger el autobús",
            "Trabajar hasta las 12:30",
            "Buscar un restaurante",
            "Almorzar aproximadamente una hora",
            "Regresar al trabajo",
            "Trabajar",
            "Salir de trabajar",
            "Coger el autobús",
            "Regresar a la casa",
            "Preparar la cena",
            "Quitarse la ropa",
            "Ponerse algo cómodo",
            "Comer",
            "Ver la televisión: op",
            "Irse a dormir"
        ],
        "puntaje": 10,  # Puntaje asignado a esta tarea
    },
    {
        "nombre": "Tarea 2",
        "descripcion": "Día de trabajo en casa.",
        "instrucciones": [
            "Levantarse temprano",
            "Cepillar los dientes",
            "Preparar una taza de café o té",
            "Configurar el espacio de trabajo en casa",
            "Comenzar a trabajar",
            "Tomar pausas regulares para estirarse",
            "Almorzar en casa",
            "Continuar trabajando",
            "Terminar el trabajo",
            "Cerrar el espacio de trabajo",
            "Hacer ejercicio",
            "Cenar",
            "Relajarse antes de dormir"
        ],
        "puntaje": 8,  # Puntaje asignado a esta tarea
    },
    {
        "nombre": "Tarea 3",
        "descripcion": "Día libre y relajante.",
        "instrucciones": [
            "Levantarse tarde",
            "Tomar un desayuno especial",
            "Hacer ejercicio",
            "Almorzar en casa o en un restaurante",
            "Realizar una actividad creativa (por ejemplo, pintar o escribir)",
            "Leer un libro o revista",
            "Cocinar una cena especial",
            "Ver una película o serie",
            "Relajarse antes de dormir"
        ],
        "puntaje": 12,  # Puntaje asignado a esta tarea
    },
    {
        "nombre": "Tarea 4",
        "descripcion": "Fin de semana de actividades diversas.",
        "instrucciones": [
            "Día Sábado:",
            "  - Levantarse tarde",
            "  - Hacer una caminata al aire libre",
            "  - Almorzar en un restaurante nuevo",
            "  - Comprar víveres en el supermercado",
            "  - Realizar una actividad de ocio (por ejemplo, ver una película)",
            "Día Domingo:",
            "  - Dormir hasta tarde",
            "  - Preparar un brunch en casa",
            "  - Visitar un museo o galería de arte",
            "  - Llamar o visitar a familiares o amigos",
            "  - Hacer una cena especial en casa"
        ],
        "puntaje": 15,  # Puntaje asignado a esta tarea
    },
    {
        "nombre": "Tarea 5",
        "descripcion": "Tareas de limpieza y organización.",
        "instrucciones": [
            "Limpiar la casa",
            "Organizar el armario",
            "Hacer las compras de la semana",
            "Lavar la ropa",
            "Hacer tareas de jardinería",
            "Reorganizar muebles",
            "Hacer una lista de tareas pendientes",
            "Descansar y disfrutar de un momento de relajación"
        ],
        "puntaje": 5,  # Puntaje asignado a esta tarea
    }
]

# Función para mostrar las instrucciones de una tarea
def mostrar_instrucciones(tarea):
    print(f"Instrucciones para '{tarea['nombre']}':")
    for paso in tarea['instrucciones']:
        print(f"- {paso}")

# Contadores e historial
contador_tareas_realizadas = {tarea['nombre']: 0 for tarea in tareas}
historial_tareas_realizadas = []
puntaje_total = 0

# Programa principal
print("------------------- Iniciar programa -------------------")

while True:
    # Genera un número de tarea aleatorio
    tarea_aleatoria = random.choice(tareas)
    
    print(f"Tarea aleatoria seleccionada: {tarea_aleatoria['nombre']}")
    print(f"Descripción: {tarea_aleatoria['descripcion']}")
    input("Presiona Enter para ver las instrucciones...")
    
    mostrar_instrucciones(tarea_aleatoria)
    respuesta = input("¿Has completado esta tarea? (Si/No): ").lower()
    
    if respuesta == 'si':
        tarea_realizada = tarea_aleatoria['nombre']
        puntaje_obtenido = tarea_aleatoria['puntaje']
        contador_tareas_realizadas[tarea_realizada] += 1
        historial_tareas_realizadas.append((tarea_realizada, puntaje_obtenido))
        puntaje_total += puntaje_obtenido
    
    respuesta = input("¿Quieres ver otra tarea aleatoria? (Si/No): ").lower()
    if respuesta != 'si':
        break

# Mostrar resumen de tareas realizadas con puntajes
print("\nResumen de tareas realizadas con puntajes:")
for tarea, contador in contador_tareas_realizadas.items():
    print(f"{tarea}: {contador} veces - Puntaje total: {contador * tareas[0]['puntaje']}")

# Mostrar historial de tareas realizadas con puntajes
print("\nHistorial de tareas realizadas con puntajes:")
for tarea_realizada, puntaje_obtenido in historial_tareas_realizadas:
    print(f"{tarea_realizada} - Puntaje: {puntaje_obtenido}")

# Mostrar puntaje total
print(f"\nPuntaje Total: {puntaje_total}")

print("\n------------------- Fin del programa -------------------")
