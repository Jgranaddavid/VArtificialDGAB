import random
print("------------------- Asignacion de tareas-------------------")
#Asignacion de tareas.
tareas=[
    { "nombre":"Tarea 1",
     "descripcion":"Realizar una serie de actividades diarias a partir de esta lista",
     "instrucciones":[
         "Levantarse",
         "Irse a cepillar los dientes",
         "Tender la cama",
         "Irse a bañar",
         "Ponerse la ropa(opciones:Op1:Camisa,Traje de paño,corbata,zapatos,cinturos,reloj,pantalon,boxers,Op2:Chaqueta,Camisa,Jean,Boxers,mediasTenis,)",
         "Desayunarse",
         "Salir de la casa",
         "Coger el autobus",
         "Trabajar hasta las 12:30",
         "Buscar un restaurante",
         "Almorzar aprozimadamente una hora",
         "Regresar al trabajo",
         "Trabajar",
         "Salir de trabajar",
         "Coger el autobus",
         "Regresar a la casa",
         "Preparar la cena",
         "Quitarse la ropa",
         "Ponerse algo comodo",
         "Comer",
         "Ver la television:op",
         "Irse a dormir"
      ]
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
             ]
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
        ]
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
        ]
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
        ]
    }
    ]
# Función para mostrar las instrucciones de una tarea
def mostrar_instrucciones(tarea):
    print(f"Instrucciones para '{tarea['nombre']}':")
    for paso in tarea['instrucciones']:
        print(f"- {paso}")


# Programa principal
print("------------------- Iniciar programa -------------------")

while True:
    # Genera un número de tarea aleatorio
    tarea_aleatoria = random.choice(tareas)
    
    print(f"Tarea aleatoria seleccionada: {tarea_aleatoria['nombre']}")
    print(f"Descripción: {tarea_aleatoria['descripcion']}")
    input("Presiona Enter para ver las instrucciones...")
    
    mostrar_instrucciones(tarea_aleatoria)
    respuesta=input("Quieres ver otra tarea aleatoria(Si/No)")
    if respuesta != 'si':
        break
    