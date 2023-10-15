# En este programa se genera un numero random entre 1 y 10 y el usuario tiene que adivinarlo
import random
number = random.randint(1, 10)
guess = int(input("Adivina el numero: "))
if guess == number:
    print("Ganaste")
else:
    print("Perdiste")
    print("El numero era:", number)