def suma(num1, num2, *args):
    if args:
        return num1 + num2 + sum(args)
    else:
        return num1 + num2
def main():
    print(suma(1, 2))
    print(suma(1, 2, 3, 4, 5))
    return 0
if __name__ == '__main__':
    main()