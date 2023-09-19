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

print(----------"Admision para entrar"----------)


nombre=str(input("Ingrese su nombre"))
edad=int(input("Ingrese su edad"))
Identificacion=int(input("Ingrese su identificacion"))
#Definir la ubicacion a partir de la Zona corresponidente
ZonaA=["1","2","3","4","5"]
ZonaB=["6","7","8","9","10"]
ZonaC=["11","12","13","14","15"]
if edad >= 18:
     edad>=18 and edad<=25
     ubicacion="Zona A"
     print(ubicacion,ZonaA)
     
elif edad>=26 and edad<=34:
     ubicacion="Zona B"
     print(ubicacion,ZonaB)
else:
      ubicacion="Zona C" 
      print(ubicacion,ZonaC)
datos=(nombre,edad,Identificacion,ubicacion)
print(datos)
