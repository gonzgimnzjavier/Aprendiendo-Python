# Este programa genera un numero aleatorio entre 1 y 10 y el usuario debe adivinarlo
import random
# while True el bucle se repite mientras se cumpla la condición
while True:
    number = random.randint(1, 10)
    guess = 0

    while guess != number:
        guess = int(input("Adivina el número entre 1 y 10: "))
        if guess < 1 or guess > 10:
            print("El número debe estar entre 1 y 10.")
            if guess == 666:
                print("Sin embargo, has elegido el número de la bestia.")
            elif guess == -666:
                print("Sin embargo, has elegido el número de la bestia invertido eso es doblemente maligno.")
        elif guess > number:
            print("El número es menor.")
        elif guess < number:
            print("El número es mayor.")

    print("¡Ganaste!")

    play_again = input("¿Quieres jugar de nuevo? (s/n): ")
    if play_again.lower() != "s":
        break
