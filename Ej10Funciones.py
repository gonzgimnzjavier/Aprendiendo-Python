import random
def guess_number_between_1_and_100():
    number = random.randint(1, 100)
    guess = 0

    while guess != number:
        guess = int(input("Ingresa un numero: "))
        if guess < 1 or guess > 100:
            print("El numero debe estar entre 1 y 100.")
        elif guess > number:
            print("El numero es menor.")
        elif guess < number:
            print("El numero es mayor.")

    print("¡Adivinaste!")

def main():
    guess_number_between_1_and_100()
    return 0
if __name__ == '__main__':
    main()