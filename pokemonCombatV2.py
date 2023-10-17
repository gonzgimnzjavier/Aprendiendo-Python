import os
from random import randint


VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 95

TAMANIO_BARRA_VIDA = 20
vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

# Esta funcion es para limpiar la consola
# Si el sistema operativo es Windows, utiliza el comando "cls"
# para borrar la pantalla.
# De lo contrario, utiliza el comando "clear".
def limpiar_consola():
    os.system("clear")

while vida_pikachu > 0 and vida_squirtle > 0:


    if vida_pikachu <= 0 or vida_squirtle <= 0:
        break

    # Turno de Pikachu
    print("\nTurno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # Bola voltio
        print("Pikachu ataca con Bola Voltio")
        vida_squirtle -= 10
    else:
        # Onda Trueno
        print("Pikachu ataca con Onda Trueno")
        vida_squirtle -= 11
    if vida_squirtle <= 0:
        vida_squirtle = 0

    barras_de_vida_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle: [{}{}] ({}/{})".format("*" * barras_de_vida_squirtle,
                                            " " * (TAMANIO_BARRA_VIDA - barras_de_vida_squirtle),
                                            vida_squirtle, VIDA_INICIAL_SQUIRTLE))
    barras_de_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu: [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                           " " * (TAMANIO_BARRA_VIDA - barras_de_vida_pikachu),
                                           vida_pikachu, VIDA_INICIAL_PIKACHU))
    input("Presiona una enter para continuar...\n")

    # Se limpia la consola
    limpiar_consola()
    # Turno de Squirtle
    print("Turno de Squirtle")
    ataque_squirtle = None

    # Si el usuario selecciona una opción diferente, se le preguntará de nuevo hasta que elija una válida
    while ataque_squirtle not in ["P", "A", "B", "S"]:
        ataque_squirtle = input("¿Qué ataque deseas realizar?\n[P]lacaje, Pistola [A]gua, [B]urbuja, [S]altar Turno: ").upper()

    if ataque_squirtle == "P":
        # Placaje
        print("Squirtle utiliza Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        # Pistola Agua
        print("Squirtle utiliza Pistola Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        # Burbuja
        print("Squirtle utiliza Burbuja")
        vida_pikachu -= 9
    else:
        # Saltar Turno
        print("Squirtle permanece quieto")
    if vida_pikachu <= 0:
        vida_pikachu = 0

    barras_de_vida_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle: [{}{}] ({}/{})".format("*" * barras_de_vida_squirtle,
                                            " " * (TAMANIO_BARRA_VIDA - barras_de_vida_squirtle),
                                            vida_squirtle, VIDA_INICIAL_SQUIRTLE))
    barras_de_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu: [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                           " " * (TAMANIO_BARRA_VIDA - barras_de_vida_pikachu),
                                           vida_pikachu, VIDA_INICIAL_PIKACHU))
    input("Presiona una enter para continuar...\n")

    # Se limpia la consola
    limpiar_consola()
# Verificar quién ha ganado
if vida_pikachu > vida_squirtle:
    print("¡Squirtle ha sido derrotado!")
    print("Pikachu ha ganado")
else:
    print("¡Pikachu ha sido derrotado!")
    print("Squirtle ha ganado")
