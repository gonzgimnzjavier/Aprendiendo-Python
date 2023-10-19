# Este programa crea la tabla de multiplicar de cualquier numero introducido por el usuario
# mostrando unicamente aquellos numeros multiplos de 2
numero = int(input("Introduce un numero: "))
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{numero} x {i} = {numero*i}")
