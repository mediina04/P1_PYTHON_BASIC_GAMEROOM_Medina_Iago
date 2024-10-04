import random


def menuPrincipal():
    print("Bienvenido a la Sala de Juegos!")
    print("Selecciona un juego:")
    print("1. Adivina el número")
    print("2. Piedra, Papel, Tijeras")
    print("3. El Ahorcado")
    print("0. Salir")

    while True:
        opcion = input("Introduce el número del juego que quieres jugar: ")
        if opcion == "1":
            adivinaNumero()
        elif opcion == "2":
            piedraPapelTijeras()
        elif opcion == "3":
            ahorcado()
        elif opcion == "0":
            print("Gracias por jugar! Hasta pronto!")
            break
        else:
            print("Opción no válida. Porfavor, selecciona una opción válida.")


### Juego 1: Adivina el número

def adivinaNumero():
    numeroSecreto = random.randint(1, 10)
    intentos = 3

    print("\nTienes que adivinar un número del 1 al 10. Tienes 3 intentos.")

    for intent in range(intentos):
        while True:
            try:
                eleccion = int(input(f"Introduce tu número (Intento {intentos + 1}): "))
                if eleccion < 1 or eleccion > 10:
                    print("Número fuera de rango. Escoge un número entre 1 y 10.")
                else:
                    break
            except ValueError:
                print("Porfavor, introduce un número válido.")

        if eleccion == numeroSecreto:
            print(f"Felicidades! Has adivinado el número: {numeroSecreto}")
            break
        elif eleccion < numeroSecreto:
            print("El número és más grande.")
        else:
            print("El número és más pequeño.")

    else:
        print(f"Lo siento, no lo has adivinado. El número era {numeroSecreto}.\n")


### Juego 2: Piedra, Papel, Tijeras

def piedraPapelTijeras():
    opciones = ["piedra", "papel", "tijeras"]
    puntosUsuario = 0
    puntosOrdenador = 0
    ganador = 3

    print("\nComenzamos el juego de Piedra, Papel, Tijeras! Gana el primero que llegue a 3 puntos.")

    while puntosUsuario < ganador and puntosOrdenador < ganador:
        eleccionUsuario = input("Piedra, papel o tijeras? ").lower()
        if eleccionUsuario not in opciones:
            print("Opción no válida. Escoge entre 'piedra', 'papel' o 'tijeras'.")
            continue

        eleccionOrdenador = random.choice(opciones)
        print(f"El ordenador ha escogido: {eleccionOrdenador}")

        if eleccionUsuario == eleccionOrdenador:
            print("Empate!")
        elif (eleccionUsuario == "piedra" and eleccionOrdenador == "tijeras") or \
                (eleccionUsuario == "papel" and eleccionOrdenador == "piedra") or \
                (eleccionUsuario == "tijeras" and eleccionOrdenador == "papel"):
            print("Has ganado este punto!")
            puntosUsuario += 1
        else:
            print("El ordenador gana este punto!")
            puntosOrdenador += 1

        print(f"Puntos: Usuario {puntosUsuario} - Ordenador {puntosOrdenador}")

    if puntosUsuario == ganador:
        print("Felicidades! Has ganado el juego!\n")
    else:
        print("El ordenador ha ganado el juego. Más suerte la próxima vez!\n")


### Juego 3: El Ahorcado

def ahorcado():
    with open("Palabras", "r") as fichero:
        palabras = [palabra.strip() for palabra in fichero.readlines() if 3 <= len(palabra.strip()) <= 7]

    palabraSecreta = random.choice(palabras).lower()
    intentos = len(palabraSecreta) * 2
    letrasAdivinadas = ["_"] * len(palabraSecreta)
    letrasUsadas = set()

    print("\nBienvenido al juego del Ahorcado!")
    print(f"La palabra tiene {len(palabraSecreta)} letras. Tienes {intentos} intentos para adivinarla.")

    while intentos > 0 and "_" in letrasAdivinadas:
        print(" ".join(letrasAdivinadas))
        print(f"Letras utilizadas: {', '.join(sorted(letrasUsadas))}")
        letra = input("Introduce una letra o intenta adivinar la palabra: ").lower()

        if len(letra) > 1:
            if letra == palabraSecreta:
                letrasAdivinadas = list(palabraSecreta)
                break
            else:
                intentos -= 1
                print(f"Incorrecto! La palabra no es {letra}. Te quedan {intentos} intentos.")

        elif letra in letrasUsadas:
            print(f"Ya has utilizado la letra '{letra}'. Prueba con otra.")
        elif letra in palabraSecreta:
            for i, car in enumerate(palabraSecreta):
                if car == letra:
                    letrasAdivinadas[i] = letra
            print(f"Correcto! La letra '{letra}' esta en la palabra.")
        else:
            intentos -= 1
            print(f"Incorrecto! Te quedan {intentos} intentos.")

        letrasUsadas.add(letra)

    if "_" not in letrasAdivinadas:
        print(f"Felicidades! Has adivinado la palabra: {palabraSecreta}\n")
    else:
        print(f"Lo siento, has perdido. La palabra era: {palabraSecreta}\n")


if __name__ == "__main__":
    menuPrincipal()

