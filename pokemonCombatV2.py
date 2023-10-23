import os
from random import randint, choice


# Funciones de combate
def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


def combate_pokemon(pokemon_oponente):
    VIDA_INICIAL_PIKACHU = 80
    VIDA_INICIAL_OPONENTE = 95
    TAMANIO_BARRA_VIDA = 20
    vida_pikachu = VIDA_INICIAL_PIKACHU
    vida_oponente = VIDA_INICIAL_OPONENTE

    while vida_pikachu > 0 and vida_oponente > 0:
        # Turno de Pikachu
        print("\nTurno de Pikachu")
        print("1. Bola Voltio")
        print("2. Onda Trueno")
        ataque_pikachu = int(input("Elige un ataque (1/2): "))
        if ataque_pikachu == 1:
            print("Pikachu ataca con Bola Voltio")
            vida_oponente -= 10
        else:
            print("Pikachu ataca con Onda Trueno")
            vida_oponente -= 11

        if vida_oponente <= 0:
            vida_oponente = 0

        print(
            f"{pokemon_oponente['name']}: [{'*' * int(vida_oponente * TAMANIO_BARRA_VIDA / VIDA_INICIAL_OPONENTE)}{' ' * (TAMANIO_BARRA_VIDA - int(vida_oponente * TAMANIO_BARRA_VIDA / VIDA_INICIAL_OPONENTE))}] ({vida_oponente}/{VIDA_INICIAL_OPONENTE})")
        print(
            f"Pikachu: [{'*' * int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)}{' ' * (TAMANIO_BARRA_VIDA - int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU))}] ({vida_pikachu}/{VIDA_INICIAL_PIKACHU})")

        input("Presiona enter para continuar...")
        limpiar_consola()

        # Turno del oponente si sigue con vida
        if vida_oponente > 0:
            print(f"Turno de {pokemon_oponente['name']}")
            ataque_oponente = randint(1, 3)
            if ataque_oponente == 1:
                print(f"{pokemon_oponente['name']} utiliza Placaje")
                vida_pikachu -= 10
            elif ataque_oponente == 2:
                print(f"{pokemon_oponente['name']} utiliza Pistola Agua")
                vida_pikachu -= 12
            else:
                print(f"{pokemon_oponente['name']} utiliza Burbuja")
                vida_pikachu -= 9

            if vida_pikachu <= 0:
                vida_pikachu = 0

            print(
                f"{pokemon_oponente['name']}: [{'*' * int(vida_oponente * TAMANIO_BARRA_VIDA / VIDA_INICIAL_OPONENTE)}{' ' * (TAMANIO_BARRA_VIDA - int(vida_oponente * TAMANIO_BARRA_VIDA / VIDA_INICIAL_OPONENTE))}] ({vida_oponente}/{VIDA_INICIAL_OPONENTE})")
            print(
                f"Pikachu: [{'*' * int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)}{' ' * (TAMANIO_BARRA_VIDA - int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU))}] ({vida_pikachu}/{VIDA_INICIAL_PIKACHU})")

            input("Presiona enter para continuar...")
            limpiar_consola()

    if vida_pikachu > vida_oponente:
        print(f"{pokemon_oponente['name']} ha sido derrotado!")
        print("Pikachu ha ganado")
        return True
    else:
        print("Pikachu ha sido derrotado!")
        print(f"{pokemon_oponente['name']} ha ganado")
        return False


# Código principal del laberinto y juego
laberinto = [
    [" ", " ", " ", "@", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", "@", " ", " ", " ", "@", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", "@", " ", "@", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "*", " ", " ", " "],
]

posicion_jugador = [6, 3]
enemigos = [{"name": "Charmander", "vida": 95}, {"name": "Bulbasaur", "vida": 95}, {"name": "Squirtle", "vida": 95}]

while True:
    limpiar_consola()
    for y in range(len(laberinto)):
        for x in range(len(laberinto[y])):
            if [y, x] == posicion_jugador:
                print("P", end="")
            else:
                print(laberinto[y][x], end="")
        print()

    movimiento = input("Movimiento (WASD): ").upper()

    nueva_posicion = list(posicion_jugador)
    if movimiento == "W":
        nueva_posicion[0] -= 1
    elif movimiento == "A":
        nueva_posicion[1] -= 1
    elif movimiento == "S":
        nueva_posicion[0] += 1
    elif movimiento == "D":
        nueva_posicion[1] += 1

    if 0 <= nueva_posicion[0] < len(laberinto) and 0 <= nueva_posicion[1] < len(laberinto[0]):
        contenido_casilla = laberinto[nueva_posicion[0]][nueva_posicion[1]]

        if contenido_casilla == " ":
            posicion_jugador = nueva_posicion
        elif contenido_casilla == "@":
            enemigo = choice(enemigos)
            resultado = combate_pokemon(enemigo)
            if resultado:
                laberinto[nueva_posicion[0]][nueva_posicion[1]] = " "
                posicion_jugador = nueva_posicion
            else:
                break

    if posicion_jugador == [0, 3]:
        print("¡Has ganado y salido del laberinto!")
        break
