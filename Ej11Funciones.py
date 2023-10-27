shopping_list = ["pan", "leche", "queso", "huevos"]

def add_item(item):
    if item not in shopping_list:
        shopping_list.append(item)
    else:
        print(item, "ya esta en la lista")

def main():
    add_item("pan")
    print(shopping_list)
    return 0
if __name__ == '__main__':
    main()
    #sys.exit(main())
