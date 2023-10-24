def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a+b
def main():
    n = int(input("Ingresa un numero: "))
    fibonacci(n)
    return 0
if __name__ == '__main__':
    main()
