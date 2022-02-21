import consultar as c
import anadir as a
import borrar as b
import os


def menuPrincipal(op: int):
    match(op):
        case 1:
            c.menuConsultar()
        case 2:
            a.menuAnadir()
        case 3:
            b.menuBorrar()
        case 4:
            print('\nCerrando aplicacion...')
            pass


def menuSecundario():
    print('¿Que quieres hacer?')
    opcion = int(
        input('\n1.Consultar Recetas\n2.Añadir Recetas\n3.Borrar Recetas\n4.Salir\n'))
    menuPrincipal(opcion)

# Esta funcion se encarga de quitar el .txt  a los ficheros


def separarCadenas(dir: str):
    listadoDirectorio = os.listdir(dir)
    listadoLimpio = []
    for receta in listadoDirectorio:
        x = receta.split('.')
        listadoLimpio.append(x[0])
    return listadoLimpio


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# Quick Sort to classify the titles of the recipes in alphabet order
def quickSortCategories(list: list, low: int, high: int):
    if len(list) == 1:
        return list
    if low < high:

        # pi is partitioning index, list[p] is now
        # at right place
        pi = partition(list, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSortCategories(list, low, pi-1)
        quickSortCategories(list, pi+1, high)

# The main function of quicksort


def partition(list: list, low: int, high: int):
    i = (low-1)         # index of smaller element
    pivot = list[high]     # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if list[j] <= pivot:

            # increment index of smaller element
            i = i+1
            list[i], list[j] = list[j], list[i]

    list[i+1], list[high] = list[high], list[i+1]
    return (i+1)

# Binary search after sort the array
def binarySearch(list : list, low : int, high : int, search : str):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if list[mid] == search:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif list[mid] > search:
            return binarySearch(list, low, mid - 1, search)
        # Else the element can only be present in right subarray
        else:
            return binarySearch(list, mid + 1, high, search)
    else:
        # Element is not present in the array
        return -1
