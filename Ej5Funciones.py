def string_mas_larga(string1, *args):
    if args:
        return max(string1, *args, key=len)
    else:
        return string1

def main():
    print(string_mas_larga("hola", "asamfkafksakf", "ok", "adios"))
    return 0
if __name__ == '__main__':
    main()
