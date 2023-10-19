# Este programa crea la tabla de multiplicar de cualquier numero introducido por el usuario
numero = int(input("Introduce un numero: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero*i}")
