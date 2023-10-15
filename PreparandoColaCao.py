#Este programa indica los pasos para preparar un ColaCao mediante estructuras de control
print("Ir a la nevera")
print("Abrir la nevera")
hayLeche = input("¿Hay leche en la nevera?(s/n)").lower() # Me permite que el input metido por el usuario no se case sensible
hayColaCao = input("¿Hay ColaCao en la ColaCao?(s/n)").lower()
#Condicionales en Python"
if hayLeche == "s" and hayColaCao == "s":
    print("Preparando ColaCao...")
    print("¡ColaCao listo!")
else:
    if hayLeche != "s":
        print("Compro leche")
    if hayColaCao != "s":
        print("Compro ColaCao")
    print("Vuelvo a casa del supermercado")
    print("Preparando ColaCao...")
    print("¡ColaCao listo!")
