SALIDA = "SALIR"

def preguntar_producto_usuario():
    return input("Ingresa un producto: [{} para salir] ".format(SALIDA)).upper()

def generar_lista_de_la_compra():
    listaDeLaCompra = []
    listaPreestablecida = ["LECHE", "QUESO", "HUEVOS", "PAN"]
    input_usuario = preguntar_producto_usuario()
    while input_usuario != SALIDA:
        if input_usuario in listaPreestablecida:
            listaDeLaCompra.append(input_usuario)
            print("\n".join(listaDeLaCompra))
            input_usuario = preguntar_producto_usuario()
        else:
            print("El producto no esta en la lista preestablecida")
            input_usuario = preguntar_producto_usuario()

    with open("listaDeLaCompra.txt", "w") as a:
        a.write("\n".join(listaDeLaCompra))

    return 0

def mostrar_lista_de_la_compra():
    try:
        with open("listaDeLaCompra.txt", "r") as a:
            print(a.read())
    except FileNotFoundError:
        print("El archivo listaDeLaCompra.txt no existe.")

    return 0

def main():
    generar_lista_de_la_compra()
    mostrar_lista_de_la_compra()

if __name__ == '__main__':
    main()
