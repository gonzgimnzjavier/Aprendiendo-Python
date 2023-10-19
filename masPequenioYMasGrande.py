# programa que encuentra dentro de una lista de números introducidos por el usuario y nos diga
# el valor más pequeño y el más grande.
colencion = []
while True:
    numero = input("Introduce un numero: (s para salir) ").lower()
    # Si el numero es un entero
    if numero.isnumeric():
        colencion.append(numero)
    elif numero == "s":
        break
print("El valor mas grande es: ", max(colencion))
print("El valor mas pequeño es: ", min(colencion))