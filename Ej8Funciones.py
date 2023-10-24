def estas_seguro ():
    seguro = True
    pregunta=input("¿Está seguro? (s/n)").lower()
    if pregunta == "s":
        seguro = True
    else:
        seguro = False
    return seguro

def main():
    print(estas_seguro())
    return 0
if __name__ == '__main__':
    main()