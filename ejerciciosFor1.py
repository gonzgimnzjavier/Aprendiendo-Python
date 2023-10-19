# Programa que dada una cadena nos diga si es el numero de puntos, comas y espacios
cadena = input("Introduce una cadena: ")

numeroDePuntos = 0
numeroDeComas = 0
numeroDeEspacios = 0

for i in cadena:
    if i == ".":
        numeroDePuntos += 1
    elif i == ",":
        numeroDeComas += 1
    elif i == " ":
        numeroDeEspacios += 1

print("La cadena tiene", numeroDePuntos, "puntos, ", numeroDeComas, "comas y ", numeroDeEspacios, "espacios")
