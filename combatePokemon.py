from random import randint
# Declaracion de variables
# Se define la vida de cada uno de los Pokemon
vidaPikachu = 80
vidaSquirtle = 90
# Se crea una cadena para adornar cada turno en la consola
turnoPikachu = "Turno de Pikachu"
turnoSquirtle = "Turno de Squirtle"
# multiplicador especifico para este pokemon
# dicho multiplicador ayudara a decrementar la barra de vida cuando sea necesario
multiploPikachu = 10
while vidaPikachu > 0 and vidaSquirtle > 0:
    # Se desarrolla el combate
    # Turno de Pikachu
    print("."*len(turnoPikachu))
    print(turnoPikachu)
    print("."*len(turnoPikachu))
    # El pikachu atacara aleatoriamente dependiendo del numero de ataques que este tenga, en este caso 2
    ataquePikachu = randint(1, 2)
    # Condiciones si hace el ataque 1
    if ataquePikachu == 1:
        # Bola voltio
        print("Pikachu utiliza Bola voltio\n")
        # Este es el daño que recibe el pokemon del jugador si usan Bola voltio
        vidaSquirtle -= 10
        if vidaSquirtle < 90 and vidaSquirtle >= 81:
            # Definimos un multiplicador especifco para este Pokemon que ayudara a decrementar la barra de vida en cada caso
            # Esto lo hará aplicando porcentajes
            multiploSquirtle = 10
            multiploSquirtle *= 0.9
        elif vidaSquirtle < 81 and vidaSquirtle >= 72:
            multiploSquirtle = 10
            multiploSquirtle *= 0.8
        elif vidaSquirtle < 72 and vidaSquirtle >= 63:
            multiploSquirtle = 10
            multiploSquirtle *= 0.7
        elif vidaSquirtle < 63 and vidaSquirtle >= 54:
            multiploSquirtle = 10
            multiploSquirtle *= 0.6
        elif vidaSquirtle < 54 and vidaSquirtle >= 45:
            multiploSquirtle = 10
            multiploSquirtle *= 0.5
        elif vidaSquirtle < 45 and vidaSquirtle >= 36:
            multiploSquirtle = 10
            multiploSquirtle *= 0.4
        elif vidaSquirtle < 36 and vidaSquirtle >= 27:
            multiploSquirtle = 10
            multiploSquirtle *= 0.3
        elif vidaSquirtle < 27 and vidaSquirtle >= 18:
            multiploSquirtle = 10
            multiploSquirtle *= 0.2
        elif vidaSquirtle < 18 and vidaSquirtle >= 1:
            multiploSquirtle = 10
            multiploSquirtle *= 0.1
        # Si la vida de Squirtle es menor que 0 esta se igulara a dicho numero
        elif vidaSquirtle <= 0:
            # Con esto evitamos que en la consola aparezcan valores negativos
            vidaSquirtle = 0
            # Iugualando el multiplo a 0 conseguiremos que cuando la vida sea 0 la barra de vida este vacia
            multiploSquirtle = 0
    else:
        # Onda Trueno
        print("Pikachu utiliza Onda Trueno\n")
        vidaSquirtle -= 9
        if vidaSquirtle < 90 and vidaSquirtle >=81:
            multiploSquirtle = 10
            multiploSquirtle *= 0.9
        elif vidaSquirtle < 81 and vidaSquirtle >=72:
            multiploSquirtle = 10
            multiploSquirtle *= 0.8
        elif vidaSquirtle < 72 and vidaSquirtle >=63:
            multiploSquirtle = 10
            multiploSquirtle *= 0.7
        elif vidaSquirtle < 63 and vidaSquirtle >=54:
            multiploSquirtle = 10
            multiploSquirtle *= 0.6
        elif vidaSquirtle < 54 and vidaSquirtle >=45:
            multiploSquirtle = 10
            multiploSquirtle *= 0.5
        elif vidaSquirtle < 45 and vidaSquirtle >=36:
            multiploSquirtle = 10
            multiploSquirtle *= 0.4
        elif vidaSquirtle < 36 and vidaSquirtle >=27:
            multiploSquirtle = 10
            multiploSquirtle *= 0.3
        elif vidaSquirtle < 27 and vidaSquirtle >=18:
            multiploSquirtle = 10
            multiploSquirtle *= 0.2
        elif vidaSquirtle < 18 and vidaSquirtle >=1:
            multiploSquirtle = 10
            multiploSquirtle *= 0.1
        elif vidaSquirtle <= 0:
            vidaSquirtle = 0
            multiploSquirtle = 0
    # casteo a entero int para realizar la multiplicacion de una cadena
    multiploSquirtle = int(multiploSquirtle)
    # Imprime por consola la barra de vida la cantidad y el nombre de cada pokemon
    print("Squirtle ["+"#"*multiploSquirtle+"]", vidaSquirtle, "Pikachu ["+"#"*multiploPikachu+"]", vidaPikachu)
    # Fin del turno de Pikachu
    # Turno de Squirtle
    if  vidaPikachu > 0 and vidaSquirtle > 0:
        print("."*len(turnoSquirtle))
        print(turnoSquirtle)
        print("."*len(turnoSquirtle))
        ataqueSquirtle = None
        # Si el usuario seleciona una opcion diferente se le volvera a preguntar hasta que escoja una valida
        while ataqueSquirtle not in ["P", "A", "B"]:
            ataqueSquirtle = input("¿Qué ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja").upper()
            if ataqueSquirtle == "P":
                # Placaje
                print("Squirtle utiliza Placaje\n")
                vidaPikachu -= 10
                if vidaPikachu < 80 and vidaPikachu >=72:
                    multiploPikachu = 10
                    multiploPikachu *= 0.9
                elif vidaPikachu < 72 and vidaPikachu >=64:
                    multiploPikachu = 10
                    multiploPikachu *= 0.8
                elif vidaPikachu < 64 and vidaPikachu >=56:
                    multiploPikachu = 10
                    multiploPikachu *= 0.7
                elif vidaPikachu < 56 and vidaPikachu >=48:
                    multiploPikachu = 10
                    multiploPikachu *= 0.6
                elif vidaPikachu < 48 and vidaPikachu >=40:
                    multiploPikachu = 10
                    multiploPikachu *= 0.5
                elif vidaPikachu < 40 and vidaPikachu >=32:
                    multiploPikachu = 10
                    multiploPikachu *= 0.4
                elif vidaPikachu < 32 and vidaPikachu >=24:
                    multiploPikachu = 10
                    multiploPikachu *= 0.3
                elif vidaPikachu < 24 and vidaPikachu >=16:
                    multiploPikachu = 10
                    multiploPikachu *= 0.2
                elif vidaPikachu < 16 and vidaPikachu >=1:
                    multiploPikachu = 10
                    multiploPikachu *= 0.1
                elif vidaPikachu <= 0:
                    vidaPikachu = 0
                    multiploPikachu = 0
            elif ataqueSquirtle == "A":
                # Burbuja
                print("Squirtle utiliza Pistola Agua\n")
                vidaPikachu -= 9
                if vidaPikachu < 80 and vidaPikachu >= 72:
                    multiploPikachu = 10
                    multiploPikachu *= 0.9
                elif vidaPikachu < 72 and vidaPikachu >= 64:
                    multiploPikachu = 10
                    multiploPikachu *= 0.8
                elif vidaPikachu < 64 and vidaPikachu >= 56:
                    multiploPikachu = 10
                    multiploPikachu *= 0.7
                elif vidaPikachu < 56 and vidaPikachu >= 48:
                    multiploPikachu = 10
                    multiploPikachu *= 0.6
                elif vidaPikachu < 48 and vidaPikachu >= 40:
                    multiploPikachu = 10
                    multiploPikachu *= 0.5
                elif vidaPikachu < 40 and vidaPikachu >= 32:
                    multiploPikachu = 10
                    multiploPikachu *= 0.4
                elif vidaPikachu < 32 and vidaPikachu >= 24:
                    multiploPikachu = 10
                    multiploPikachu *= 0.3
                elif vidaPikachu < 24 and vidaPikachu >= 16:
                    multiploPikachu = 10
                    multiploPikachu *= 0.2
                elif vidaPikachu < 16 and vidaPikachu >= 1:
                    multiploPikachu = 10
                    multiploPikachu *= 0.1
                elif vidaPikachu <= 0:
                    vidaPikachu = 0
                    multiploPikachu = 0
            elif ataqueSquirtle == "B":
                # Burbuja
                print("Squirtle utiliza Burbuja\n")
                vidaPikachu -= 8
                if vidaPikachu < 80 and vidaPikachu >= 72:
                    multiploPikachu = 10
                    multiploPikachu *= 0.9
                elif vidaPikachu < 72 and vidaPikachu >= 64:
                    multiploPikachu = 10
                    multiploPikachu *= 0.8
                elif vidaPikachu < 64 and vidaPikachu >= 56:
                    multiploPikachu = 10
                    multiploPikachu *= 0.7
                elif vidaPikachu < 56 and vidaPikachu >= 48:
                    multiploPikachu = 10
                    multiploPikachu *= 0.6
                elif vidaPikachu < 48 and vidaPikachu >= 40:
                    multiploPikachu = 10
                    multiploPikachu *= 0.5
                elif vidaPikachu < 40 and vidaPikachu >= 32:
                    multiploPikachu = 10
                    multiploPikachu *= 0.4
                elif vidaPikachu < 32 and vidaPikachu >= 24:
                    multiploPikachu = 10
                    multiploPikachu *= 0.3
                elif vidaPikachu < 24 and vidaPikachu >= 16:
                    multiploPikachu = 10
                    multiploPikachu *= 0.2
                elif vidaPikachu < 16 and vidaPikachu >= 1:
                    multiploPikachu = 10
                    multiploPikachu *= 0.1
                elif vidaPikachu <= 0:
                    vidaPikachu = 0
                    multiploPikachu = 0
            multiploPikachu = int(multiploPikachu)
            print("Squirtle ["+"#"*multiploSquirtle+"]", vidaSquirtle, "Pikachu ["+"#"*multiploPikachu+"]", vidaPikachu)
            # Fin del turno de Sqirtle
# El pokemon que tenga mas vida al final del combate es el vencedor
if vidaPikachu > vidaSquirtle:
    print("¡Sqirtle ha sido derrotado!")
    print("Pikachu ha ganado")
else:
    print("¡Pikachu ha sido derrotado!")
    print("Sqirtle ha ganado")
