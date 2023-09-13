#Este programa va a tener como finalidad mezclar varios elementos que pueda solicitar el usuario o
#vamos a colocar diferentes metodos para poder realizar actividades simples o secuenciales
#del mismo modo permitira realizar salidas de informacion sujetas a condiciones logicas

#print("---------------------------  Inicio del programa --------------------------------")

#Edad1= int(input("¿Cual es su edad"))

#if Edad1<18:

    #print("Eres menor de edad")

#else:

    #print("Es mayor de edad")


    #print("--------------------------------------Modulo de seguridad--------------------------------------")


#Aca el usuario una vez eatablece si es mayor de edad, le vamos a soicitar una contraseña



#print("Su contraseña fue enviada exitosamente en su correo")


#ClaveMayorEdad = "Contraseña "
#password = input ("Ingrese la contraseña que fue enviada a su correo")

#if ClaveMayorEdad== password.lower():
      #print("Contraseña o password correcto")
#else:
     #print("Contraseña incorrecta")

#print ("------------------------------------------------- Modulo 3 de interaccion----------------------")

#print ("Escriba una frase o palabra para seguir adelante en la autenticacion")

#frase=input("Introduce una frase")

#Si se desea reemplazar la contraseña solicite al usuario esceibir en diferentes letras y numeros
#la nueva contraseña o simplemente solicite un parametro de validacion


#vocal= input ("Introduzca una vocal en minuscula")

#print(frase.replace(vocal, vocal.upper))

#print("Usted ha completado los tres modulos de autenticacion / puede seguir adelante con el pago ")






#Mejora del programa 






print("---------------------------  Inicio del programa --------------------------------")

Edad1 = int(input("¿Cuál es su edad? "))

if Edad1 < 18:
    print("Eres menor de edad")
else:
    print("Es mayor de edad")

    print("-------------------------------------- Módulo de seguridad --------------------------------------")

    # Aquí, se envía una contraseña a su correo, asumiremos que la contraseña es "Contraseña"
    ClaveMayorEdad = "Contraseña"
    password_correcta = False

    while not password_correcta:
        password = input("Ingrese la contraseña que fue enviada a su correo: ")

        if ClaveMayorEdad == password:
            print("Contraseña correcta")
            password_correcta = True
        else:
            print("Contraseña incorrecta. Inténtelo nuevamente.")

    print("------------------------------------------------- Módulo 3 de interacción ----------------------")

    print("Escriba una frase o palabra para seguir adelante en la autenticación")

    frase = input("Introduce una frase: ")

    # Si se desea reemplazar la contraseña, solicite al usuario escribir una nueva contraseña o
    # simplemente solicite un parámetro de validación

    vocal = input("Introduzca una vocal en minúscula: ")

    # Utiliza el método replace para reemplazar la vocal en la frase por la versión en mayúscula
    nueva_frase = frase.replace(vocal, vocal.upper())

    print(nueva_frase)

    print("Usted ha completado los tres módulos de autenticación. Puede seguir adelante con el pago.")

