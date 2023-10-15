#Conversor de divisas
titulo = "Conversor de divisas"
print("-" * len(titulo))
print(titulo)
print("-" * len(titulo))
input("Presiona enter para comenzar")
print("")
cantidad = float(input("Introduce la cantidad de divisas a convertir: "))
opcion = (input("Elija la moneda de origen:\na) Euro\nb) Libra Esterlina\n").lower())
if opcion == "a":
    print(f"{cantidad} euros son {round(cantidad * 0.92, 2)} libras")
elif opcion == "b":
    print(f"{cantidad} libras son {round(cantidad * 1.15, 2)} euros")
else:
    print("Las monedas disponibles son a o b")
