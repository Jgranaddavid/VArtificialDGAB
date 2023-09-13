print("---------------------------  Inicio del programa --------------------------------")

Edad1 = int(input("¿Cuál es su edad? "))

if Edad1 < 18:
    print("Eres menor de edad")
else:
    print("Es mayor de edad")

    print("-------------------------------------- Módulo de seguridad --------------------------------------")

    # Aquí, se envía una contraseña a su correo y se solicita la contraseña
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

