#los ciclos para la programacion son secuenciales que permitenb la realizacion o ejecucion de un codigo
#funciones para poder abreviar o automatizar un codigo
#ciclo while que significa mientras que

""
#print("Tipo de programa que incluya un ciclo")

#print("--------------Inio del ciclo----------------------")

#for i in range (10):
    #print(i**4)

#print("Finalize el ciclo")


#El programa que vamos a realizar tiene como finalidad realiza un ciclo en donde le 
#ingresar hasta un 3 un numero, en este caso la edad, y cuando genere la variable correcta
#ejecute en pantalla la siguiente accion: digita tu numero de cedula
#saber el numero de silla donde fue asignado

print("Admisión para entrar")

while True:
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    identificacion = int(input("Ingrese su identificación: "))
    
    ubicacion = None
    
    while ubicacion is None:
        if 18 <= edad <= 25:
            ubicacion = "Zona A"
            zona = ["1", "2", "3", "4", "5"]
        elif 26 <= edad <= 34:
            ubicacion = "Zona B"
            zona = ["6", "7", "8", "9", "10"]
        else:
            ubicacion = "Zona C"
            zona = ["11", "12", "13", "14", "15"]
    
    print("Ubicación:", ubicacion)
    print("Lista de ubicación:", zona)
    
    datos = (nombre, edad, identificacion, ubicacion)
    print("Datos de admisión:", datos)
