def potencia_parametro_opcional(x, *args):
    if args:
        return x ** args[0]
    else:
        return x * x

def main():
    print(potencia_parametro_opcional(5))
    print(potencia_parametro_opcional(3, 9))
    return 0
if __name__ == '__main__':
    main()