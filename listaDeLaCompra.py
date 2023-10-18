# Realiza un programa similar al visto en la clase que añada elementos a la lista de la compra, que compruebe si hay alguno de los elementos en la lista y que los muestre.
# Utiliza a.append, in y print.
# Programa para la lista de la compra
#Creamos una lista vacia para que el usuario ingrese los productos
import os

listaDeProductos = []


while True:
    producto = input("Ingresa un producto a la lista de la compra:(Q para salir/ L para ver la lista de la compra) \n").lower()
    if producto == "q":
        print("Gracias por usar el programa")
        break
    elif producto == "l":
        print("Lista de la compra",listaDeProductos+"\n")
    else:
        opciones = input("Seguro que deseas añadir "+producto+" a la lista de la compra? (s/n)\n").lower()
        if opciones == "s":
            listaDeProductos.append(producto)
            print(producto, "agregado a la lista de la compra\n")
        else:
            pass

