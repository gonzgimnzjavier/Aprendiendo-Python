def es_impar(n):
    if n % 2 == 1:
        return True
    else:
        return False

def main():
    n = int(input("Ingresa un numero: "))
    if es_impar(n):
        print("Es impar")
    else:
        print("No es impar")
    return 0
if __name__ == '__main__':
    main()