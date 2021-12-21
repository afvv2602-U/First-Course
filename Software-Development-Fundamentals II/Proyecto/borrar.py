#Imports
import os

#Mis funciones
import funciones as f
import consultar as c
import anadir as a
#Directorio de las recetas añadidas por el usuario
directory = 'Recetas\\Tus Recetas\\'

def menuBorrar():
    f.clearConsole()
    #Revisa si el directorio que contiene las recetas esta creado
    if c.checkDirectoryPath(directory):
        print('\nNo tienes ninguna receta para borrar\n')
        op = int(input('\n1.Ir a explorar recetas\n2.Añadir una receta\n3.Salir\n'))
        match (op):
            case 1:
                c.explorar()
            case 2:
                a.menuAnadir()
            case 3:
                f.menuSecundario()
    else:
        listado = f.separarCadenas(directory)
        print('')
        print(*listado,sep='\n')
        receta = str(input('\n¿Que receta quieres borrar?\n'))
        sw=checkReceta(receta,listado)
        if sw:
            borrarReceta(receta)
            f.menuSecundario()
        else:
            print('Cancelando volviendo al menu principal')
            f.menuSecundario()
                
def checkReceta(nombre : str , listado : list):
    for x in listado:
        if nombre.title() == x.title():
            print('\n¿Estas seguro de que quieres borrar la receta: '+str(nombre)+'?')
            op = int(input('\n1.Si\n2.No\n'))    
            if op == 1:
                return True
            else:
                return False
    return False
        
def borrarReceta(receta):
    file = str(directory+''+receta+'.txt')
    os.remove(file)
    print('La receta '+str(receta)+'ha sido borrada con éxito')

