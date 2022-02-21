#Imports
import os
import shutil as s
import codecs as co 

#Mis funciones
from anadir import menuAnadir,cargarRecetas
import funciones as f

#Directorio de las recetas añadidas por el usuario
directoryTR = 'Recetas\\Tus Recetas\\'

#Directorio de las recetas del explorar
directoryEX = 'Recetas\\Explorar\\'

def menuConsultar():
    f.clearConsole()
    opcion = int(input('\n1.¿Quieres consultar tus recetas?\n2.¿Quieres explorar?\n'))
    match (opcion):
        case 1:
            mostrarTusRecetas()
        case 2:
            explorar()

#Si tienes recetas te las muestra sino te permite añadir una nueva o ir a la seccion explorar
def mostrarTusRecetas():
    #Vemos si existe el directorio de nuestras recetas
    if checkDirectoryPath(directoryTR):
        print('\nNo tienes ninguna receta.')
        op = int(input('1.¿Quieres añadir una?\n2.¿Prefieres explorar nuestras recetas?\n'))
        if op == 1:
            f.clearConsole()
            menuAnadir()
        else:
            f.clearConsole()
            explorar()
    #Si el directorio existe entonces vamos a mostrar todas las recetas que contiene
    else:
        listado = f.separarCadenas(directoryTR)
        f.quickSortCategories(listado,0,len(listado)-1)
        print(*listado,sep='\n')
        receta = str(input('¿Que receta quieres ver?\n'))
        buscarRecetaBinario(receta,listado, sw = True)

#Muestra un listado con  las recetas que se encuentran en la seccion explorar
def explorar():
    #Si es la primera vez que se ejecuta se cargan ciertas recetas explorar ademas de crear el directorio
    if checkDirectoryPath(directoryEX):
        cargarRecetas()
        listado = f.separarCadenas(directoryEX)
        f.quickSortCategories(listado,0,len(listado)-1)
        print(*listado, sep='\n')
        receta = str(input('¿Que receta quieres ver?\n')).title()
        buscarRecetaBinario(receta,listado,sw = False)
    #Si ya existe directamente te muestran las recetas que hay dentro
    else:
        listado = f.separarCadenas(directoryEX)
        f.quickSortCategories(listado,0,len(listado)-1)
        print(*listado, sep='\n')
        receta = str(input('¿Que receta quieres ver?\n')).title()
        buscarRecetaBinario(receta,listado,sw = False)

#If boolean is true the function goes to Tus recetas directory if is False, the function goes to Explorar directory
def buscarRecetaBinario(file : str, listado : list, sw : bool):
    if sw:
        #Saving the return value and using to complete de if
        if value := f.binarySearch(list = listado,low = 0 , high = len(listado)-1, search = file) != -1:
            pathC = directoryTR + file + '.txt'
            print(pathC)
            with open(pathC,'r+',encoding="latin-1") as fi:
                print(fi.read())
            f.clearConsole()
            f.menuSecundario()
        else:
            print('\nEsa receta no se encuentra')
            op = int(input('1.¿Quieres añadirla?\n2.¿Quieres volver a ver el listado?\n3.Volver al menu\n'))
            match(op):
                case 1:
                    f.clearConsole()
                    menuAnadir()
                case 2:
                    f.clearConsole()
                    mostrarTusRecetas()
                case 3:
                    f.menuSecundario()
    else:
        #binary search return -1 if the search isn't in the array
        if value := f.binarySearch(list = listado,low = 0 , high = len(listado)-1, search = file) != -1:
            #Reconstruimos el path completo del fichero
                pathC = directoryEX + file + '.txt'
                with open(pathC,'r+',encoding="latin-1") as fi:
                    print(fi.read())   
                print('\n\n¿Quieres guardarte la receta en Tus Recetas?\n')
                op = int(input('1.Si\n2.No\n'))
                if op == 1:
                    #Copiamos el fichero del directorio explorar al directorio Tus Recetas
                    checkDirectoryPath(directoryTR)
                    s.copy(pathC,directoryTR)
                    f.clearConsole()
                    f.menuSecundario()
                else:
                    f.clearConsole()
                    f.menuSecundario()
        else:
            print('\nEsa receta no se encuentra')
            op = int(input('1.¿Quieres añadirla?\n2.¿Quieres volver a ver el listado?\n3.Volver al menu\n'))
            match(op):
                case 1:
                    f.clearConsole()
                    menuAnadir()
                case 2:
                    f.clearConsole()
                    mostrarTusRecetas()
                case 3:
                    f.menuSecundario()


#Revisa si el directorio que se va a utilizar existe y si no lo crea
def checkDirectoryPath(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    else:
        return False
                    
# #Este metodo se encarga de revisar si la receta introducida existe y si es asi te muestra la receta por pantalla
# def buscarReceta(file : str, listado : list,path : str):
#     for x in listado:
#         if file.title() == x.title():
#                 #Reconstruimos el path para poder encontrar el archivo
#                 pathC = path + file + '.txt'
#                 print(pathC)
#                 with open(pathC,'r+',encoding="utf-8") as fi:
#                     print(fi.read())
#                 f.clearConsole()
#                 f.menuSecundario()
#                 break
#         else:
#             print('\nEsa receta no se encuentra')
#             op = int(input('1.¿Quieres añadirla?\n2.¿Quieres volver a ver el listado?\n3.Volver al menu\n'))
#             match(op):
#                 case 1:
#                     f.clearConsole()
#                     menuAnadir()
#                 case 2:
#                     f.clearConsole()
#                     mostrarTusRecetas()
#                 case 3:
#                     f.menuSecundario()


# #Se encarga de buscar la receta el listado de Explorar      
# def buscarRecetaEX(file : str, listado,path : str):
#     for x in listado:
#         if file.title() == x.title():
#                 #Reconstruimos el path completo del fichero
#                 pathC = path + file + '.txt'
#                 with open(pathC,'r+',encoding="utf-8") as fi:
#                     print(fi.read())    
#                 print('\n\n¿Quieres guardarte la receta en Tus Recetas?\n')
#                 op = int(input('1.Si\n2.No\n'))
#                 if op == 1:
#                     #Copiamos el fichero del directorio explorar al directorio Tus Recetas
#                     checkDirectoryPath(directoryTR)
#                     s.copy(pathC,directoryTR)
#                     f.clearConsole()
#                     f.menuSecundario()
#                     break
#                 else:
#                     f.clearConsole()
#                     f.menuSecundario()
#                     break
#     print('\nEsa receta no se encuentra')
#     op = int(input('1.¿Quieres añadirla?\n2.¿Quieres volver a ver el listado?\n3.Volver al menu\n'))
#     match(op):
#         case 1:
#             f.clearConsole()
#             menuAnadir()
#         case 2:
#             f.clearConsole()
#             mostrarTusRecetas()
#         case 3:
#             f.menuSecundario()
            
