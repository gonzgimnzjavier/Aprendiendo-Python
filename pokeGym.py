import os
from random import randint, choice


# Función para limpiar consola
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


# Función para el combate contra un Pokémon oponente
def pokemon_combat(opponent_pokemon):
    PIKACHU_INITIAL_HP = 100
    OPPONENT_INITIAL_HP = 95
    HP_BAR_SIZE = 20
    pikachu_hp = PIKACHU_INITIAL_HP
    opponent_hp = OPPONENT_INITIAL_HP

    while pikachu_hp > 0 and opponent_hp > 0:
        # Turno de Pikachu
        valid_choice = False
        while not valid_choice:
            print("\nTurno de Pikachu")
            print("1. Bola Voltio")
            print("2. Onda Trueno")
            print("3. Pasar el turno")
            pikachu_attack = input("Elige un ataque (1/2/3): ")
            if pikachu_attack == "1":
                print("Pikachu ataca con Bola Voltio")
                opponent_hp -= 10
                valid_choice = True
            elif pikachu_attack == "2":
                print("Pikachu ataca con Onda Trueno")
                opponent_hp -= 11
                valid_choice = True
            elif pikachu_attack == "3":
                print("Pikachu decide pasar el turno")
                valid_choice = True
            else:
                print("Opción inválida. Inténtalo de nuevo.")

        # Muestra las barras de vida tras el ataque de Pikachu
        print_hp_bars(pikachu_hp, opponent_hp, opponent_pokemon, PIKACHU_INITIAL_HP, OPPONENT_INITIAL_HP)

        # Turno del oponente si aún tiene vida
        if opponent_hp > 0:
            print(f"\nTurno de {opponent_pokemon['name']}")
            opponent_attack = randint(1, 3)
            if opponent_attack == 1:
                print(f"{opponent_pokemon['name']} utiliza Placaje")
                pikachu_hp -= 8
            elif opponent_attack == 2:
                print(f"{opponent_pokemon['name']} utiliza Cuchillada")
                pikachu_hp -= 10
            else:
                print(f"{opponent_pokemon['name']} utiliza Puño Drenaje")
                pikachu_hp -= 7

            # Muestra las barras de vida tras el ataque del oponente
            print_hp_bars(pikachu_hp, opponent_hp, opponent_pokemon, PIKACHU_INITIAL_HP, OPPONENT_INITIAL_HP)

    if pikachu_hp > opponent_hp:
        print(f"{opponent_pokemon['name']} ha sido derrotado!")
        print("Pikachu ha ganado")
        return True
    else:
        print("Pikachu ha sido derrotado!")
        print(f"{opponent_pokemon['name']} ha ganado")
        return False


# Función para imprimir las barras de vida
def print_hp_bars(pikachu_hp, opponent_hp, opponent_pokemon, PIKACHU_INITIAL_HP, OPPONENT_INITIAL_HP):
    HP_BAR_SIZE = 20
    print(
        f"{opponent_pokemon['name']}: [{'*' * int(opponent_hp * HP_BAR_SIZE / OPPONENT_INITIAL_HP)}{' ' * (HP_BAR_SIZE - int(opponent_hp * HP_BAR_SIZE / OPPONENT_INITIAL_HP))}] ({opponent_hp}/{OPPONENT_INITIAL_HP})")
    print(
        f"Pikachu: [{'*' * int(pikachu_hp * HP_BAR_SIZE / PIKACHU_INITIAL_HP)}{' ' * (HP_BAR_SIZE - int(pikachu_hp * HP_BAR_SIZE / PIKACHU_INITIAL_HP))}] ({pikachu_hp}/{PIKACHU_INITIAL_HP})")
    input("Presiona enter para continuar...")
    clear_console()


# Código principal del laberinto y juego
maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "@", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "@", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "@", " ", "#", " ", "#", " ", " ", " ", "#"],
    ["#", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

player_position = [7, 3]
enemies = [{"name": "Charmander", "hp": 95}, {"name": "Bulbasaur", "hp": 95}, {"name": "Squirtle", "hp": 95}]
defeated_enemies = 0

while True:
    clear_console()
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if [y, x] == player_position:
                print("P", end="")
            else:
                print(maze[y][x], end="")
        print()

    move = input("Movimiento (WASD): ").upper()

    new_position = list(player_position)
    if move == "W":
        new_position[0] -= 1
    elif move == "A":
        new_position[1] -= 1
    elif move == "S":
        new_position[0] += 1
    elif move == "D":
        new_position[1] += 1

    if 0 <= new_position[0] < len(maze) and 0 <= new_position[1] < len(maze[0]):
        cell_content = maze[new_position[0]][new_position[1]]

        if cell_content == " ":
            player_position = new_position
        elif cell_content == "@" and len(enemies) > 0:
            enemy = enemies.pop()  # Eliminar y retornar el último Pokémon oponente
            result = pokemon_combat(enemy)
            if result:
                maze[new_position[0]][new_position[1]] = " "
                player_position = new_position
                defeated_enemies += 1
            else:
                break

    if defeated_enemies == 3:
        print("¡Has vencido a todos los entrenadores y ganado el gimnasio!")
        break
