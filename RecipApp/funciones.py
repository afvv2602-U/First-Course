import consultar as c
import anadir as a
import borrar as b
import os

def menuPrincipal(op : int):
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
    opcion = int(input('\n1.Consultar Recetas\n2.Añadir Recetas\n3.Borrar Recetas\n4.Salir\n'))
    menuPrincipal(opcion)

#Esta funcion se encarga de quitar el .txt  a los ficheros
def separarCadenas(dir : str):
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
