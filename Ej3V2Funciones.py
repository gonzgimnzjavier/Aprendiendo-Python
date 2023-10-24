def fibonacciRecursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2)

def main():
    n = int(input("Ingresa un numero: "))
    for i in range(n):
        print(fibonacciRecursivo(i), end=" ")
    return 0

if __name__ == '__main__':
    main()
