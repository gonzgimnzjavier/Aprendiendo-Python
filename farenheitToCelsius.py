#Este programa calcula la conversion de grados farenheit a celsius
print("Introduce los grados farenheit que deseas convertir:")
farenheit = float(input())
celsius = (farenheit - 32) * 5 / 9
#f indica float en la siguiente linea el numero que precede a dicha letra indica la cantidad de decimales
print(f"{farenheit} grados farenheit son {celsius:.2f} grados celsius")