import os
import readchar
import random
import time
import threading

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

snake = [[3, 1], [2, 1], [1, 1]]  # Snake inicial de tres segmentos
current_direction = "d"
stop_game = False

def generate_random_object():
    return [random.randint(0, MAP_WIDTH-1), random.randint(0, MAP_HEIGHT-1)]

map_objects = [generate_random_object() for _ in range(10)]
seen = set()
for segment in snake:
    seen.add(tuple(segment))
map_objects = [obj for obj in map_objects if tuple(obj) not in seen and not seen.add(tuple(obj))]

while len(map_objects) < 10:
    new_obj = generate_random_object()
    if tuple(new_obj) not in seen:
        map_objects.append(new_obj)
        seen.add(tuple(new_obj))

def move_snake(snake, direction):
    head = snake[0].copy()
    if direction == "w":
        head[POS_Y] = (head[POS_Y] - 1) % MAP_HEIGHT
    elif direction == "a":
        head[POS_X] = (head[POS_X] - 1) % MAP_WIDTH
    elif direction == "s":
        head[POS_Y] = (head[POS_Y] + 1) % MAP_HEIGHT
    elif direction == "d":
        head[POS_X] = (head[POS_X] + 1) % MAP_WIDTH
    snake.insert(0, head)

def input_thread():
    global current_direction, stop_game
    while not stop_game:
        direction = readchar.readchar().lower()
        if direction in ["w", "a", "s", "d"] and direction != current_direction:
            current_direction = direction
        elif direction == "q":
            stop_game = True

threading.Thread(target=input_thread).start()

# Representación en ASCII de "GAME OVER"
GAME_OVER = [
    "  _____                         ____                 ",
    " / ____|                       / __ \                ",
    "| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ ",
    "| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|",
    "| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ",
    " \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   "
]

def draw_game_over():
    start_y = (MAP_HEIGHT - len(GAME_OVER)) // 2
    start_x = (MAP_WIDTH * 3 - len(GAME_OVER[0])) // 2

    for index, line in enumerate(GAME_OVER):
        print("|" + " " * start_x + line + " " * (MAP_WIDTH * 3 - start_x - len(line)) + "|")

while not stop_game:
    os.system("clear")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "   "
            if [coordinate_x, coordinate_y] in snake:
                char_to_draw = " @ "
            else:
                for map_object in map_objects:
                    if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                        char_to_draw = " * "
                        break
            print(char_to_draw, end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    move_snake(snake, current_direction)

    if snake[0] in snake[1:]:
        os.system("clear")
        print("+" + "-" * MAP_WIDTH * 3 + "+")
        draw_game_over()
        print("+" + "-" * MAP_WIDTH * 3 + "+")
        time.sleep(2)
        break

    if snake[0] in map_objects:
        map_objects.remove(snake[0])
        new_obj = generate_random_object()
        while new_obj in snake or new_obj in map_objects:
            new_obj = generate_random_object()
        map_objects.append(new_obj)
    else:
        snake.pop()

    time.sleep(0.1)
