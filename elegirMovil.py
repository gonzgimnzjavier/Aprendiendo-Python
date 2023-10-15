# Programa que ayuda a elegir movil
opciones = ["a", "i"]
while True:
    eleccion = input("Prefieres android o ios (a/i)").lower()
    if eleccion in opciones:
        break
    else:
        print("Opcion no valida introduzca a o i")
if eleccion == "a":
    opciones = ["s", "n"]
    while True:
        eleccion = input("Tienes dinero? (s/n)")
        if eleccion in opciones:
            break
        else:
            print("Opcion no valida introduzca s o n")
    if eleccion == "s":
        opciones = ["s", "n"]
        while True:
            eleccion = input("Te importa la camara? (s/n)")
            if eleccion in opciones:
                break
            else:
                print("Opcion no valida introduzca s o n")
        if eleccion == "s":
            movilIdeal = "Google Pixel"
        else:
            movilIdeal = "Android calidad-precio"
    elif eleccion == "n":
        movilIdeal = "Android chino"
elif eleccion == "i":
    opciones = ["s", "n"]
    while True:
        eleccion = input("Tienes dinero? (s/n)")
        if eleccion in opciones:
            break
        else:
            print("Opcion no valida introduzca s o n")
    if eleccion == "s":
        movilIdeal = "Iphone Ultra Pro Max"
    else:
        movilIdeal = "Iphone de segunda mano"
print("El movil ideal para ti es:", movilIdeal)
