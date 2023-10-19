# Programa que cuenta las mayusculas
cadena = input("Introduce una cadena: ")

numeroDeMayusculas = 0

for i in cadena:
    if i.isupper():
        numeroDeMayusculas += 1
print("La cadena tiene", numeroDeMayusculas, "mayusculas")