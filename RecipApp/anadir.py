#Imports
import os

#Mis funciones
import funciones as f
import consultar as c

#Directorio de las recetas añadidas por el usuario
directory = 'Recetas\\Tus Recetas\\'
explorar = 'Recetas\\Explorar\\'

def menuAnadir():
    f.clearConsole()
    c.checkDirectoryPath(directory)
    listado = f.separarCadenas(directory)
    nombre = str(input('¿Como se llama la receta?: ')).title()
    if not listado :
        ingredientes = cargarIngredientes()
        pasos = cargarPasos()
        autor = str(input('¿Quien ha hecho esta receta?: '))
        f.clearConsole()
        crearReceta(nombre,ingredientes,pasos,autor) 
    else:
        sw,nombreRevisado = checkReceta(nombre,listado)
        if sw:
            f.clearConsole()
            c.buscarReceta(nombre,listado,directory)
        else:
            ingredientes = cargarIngredientes()
            pasos = cargarPasos()
            autor = str(input('¿Quien ha hecho esta receta?: '))
            crearReceta(nombreRevisado,ingredientes,pasos,autor) 
        
def cargarIngredientes():
    ingredientes = []
    print('\nSeccion de Ingredientes')
    while True:
        op = int(input('1.Añadir un ingrediente\n2.Salir\n'))
        if op == 1:
            ingrediente = str(input('Introduce el ingrediente: '))
            ingredientes.append(ingrediente)
        else:
            break
    return ingredientes

def cargarPasos():
    pasos = []
    print('\nSeccion Pasos')
    while True:
        op = int(input('\n1.Insertar paso\n2.Salir\n'))
        if op == 1:
            if len(pasos) == 0:
                paso = str(input('Introduce el paso numero 1: \n'))
                pasos.append(paso)
            else:
                paso = str(input('Introduce el paso numero '+str(len(pasos)+1)+': \n'))
                pasos.append(paso)
        else:
            break
    return pasos

def crearReceta(nombre : str ,ingredientes : list,pasos : list ,autor : str):
    file = str(directory+''+nombre+'.txt')
    filepath = os.path.join(file)
    with open(filepath,'x+',encoding="utf-8") as file:
        file.write('*Receta de como hacer: '+str(nombre)+' *')
        file.write('\n')
        file.write('\n')
        file.write('*Estos son los ingredientes: ')
        file.write('\n')
        for ingrediente in ingredientes:
            file.write('\t-'+str(ingrediente))
            file.write('\n')
        file.write('*')
        file.write('\n')
        file.write('*Pasos a seguir: ')
        file.write('\n')
        for i in range(len(pasos)):
            file.write('#Paso numero '+str(i+1))
            file.write('\n')
            file.write('\t~'+str(pasos[i]))
            file.write('\n')
        file.write('*')
        file.write('\n')
        file.write('*Receta creada por: '+str(autor)+' *')
    print('Volviendo al menu principal')
    f.clearConsole()
    f.menuSecundario()
        
def checkReceta(nombre : str , listado : list ):
    for x in listado:
        if nombre.title() == x.title():
                print('Tienes una receta con el mismo nombre ya añadida, ¿Quieres leerla?\n')
                op = int(input('1.Si\n2.No\n'))
                if op == 1:
                    return True,nombre
                else:
                    print('\nPara añadir la receta tienes que ponerle otro nombre')
                    name = str(input('¿Como quieres llamar la receta?: '))
                    return False,name
        else:
            return False,nombre

def cargarRecetas():
    path = os.path.join('Recetas.txt')
    with open(path,'r+',encoding="utf-8") as file:
        content=file.readlines()
        sw = True
        recetaAct = []
        for linea in content:
            if linea[0] == '&':
                sw = not sw
                if not sw:
                    nombre = separarReceta(recetaAct)
                    generarReceta(nombre,recetaAct)
                    recetaAct.clear()
                    sw = not sw    
            else:
                recetaAct.append(linea)

def separarReceta(todo : list):
    nombre = ''
    for line in todo:
        x = line.split(':')
        if len(x)> 1:
            nombre = (x[1])
            return nombre.strip()
    
def generarReceta(nombre : str,todo : list):
    if not nombre:
        pass
    else:
        file = str(explorar)+''+str(nombre)+'.txt'
        filepath = os.path.join(file)
        with open(filepath,'w+' ) as f: 
            f.writelines(todo)

