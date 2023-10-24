def a_mayusculas(s):
    resultado = ''

    for letra in s:
        # Si la letra es una letra minúscula
        if 'a' <= letra <= 'z':
            # Convertimos la letra a mayúscula usando la diferencia en ASCII
            resultado += chr(ord(letra) - 32)
        else:
            # Si no es una letra minúscula, simplemente añadimos la letra original
            resultado += letra

    return resultado

def main():
    s = input("Ingresa una cadena: ")
    print(a_mayusculas(s))
    return 0
if __name__ == '__main__':
    main()
