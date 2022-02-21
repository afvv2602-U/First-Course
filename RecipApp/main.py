from funciones import menuPrincipal, quickSortCategories, binarySearch

def main():
    print('Bienvenido a tu app de recetas:\n¿ Que quieres hacer ?')
    opcion = int(input('1.Consultar Recetas\n2.Añadir Recetas\n3.Borrar Recetas\n'))
    menuPrincipal(opcion)
    


if __name__ == "__main__":
    main()