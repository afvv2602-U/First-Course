from random import choice , randint
import os
from datetime import datetime
path = 'Practica Final\\Partidas\\'

def empezarJuego():
    capitales = {'Rusia':'Moscú','Albania':'Tirana','Alemania':'Berlín','Islandia':'Reikiavik','Bélgica':'Bruselas','Bosnia y Herzegovina':'Sarajevo',
    'Bulgaria':'Sofía','Dinamarca':'Copenhague','Eslovaquia':'Bratislava','España':'Madrid','Checa':'Praga','Rumanía':'Bucarest',
    'Grecia':'Atenas','Suecia':'Estocolmo','Finlandia':'Helsinki','Ucrania':'Kiev','Chipre':'Nicosia','Irlanda':'Dublín','Luxemburgo':'Luxemburgo','Turquía':'Ankara',
    'Italia':'Roma','Países Bajos':'Ámsterdam'}
    #Se elige un elemento aleatorio de esta lista
    op = False
    informacionPartida = []
    jugador = mensajeBienvenida()
    while True:
        informacionPartida.append('-'+juego(capitales,jugador))
        informacionPartida.append('\n')
        while True:
            opcion = str(input('¿Quieres seguir jugando? (s/n)\n'))
            if opcion[0].lower() == 's':
                break
            elif opcion[0].lower() == 'n':
                print('\nNos vemos en la proxima')
                op = True
                break
        if op:
            break
    guardarPartida(informacionPartida,jugador)
    
def mensajeBienvenida():
    informacion = {'nombre':None,'edad':None}
    print('Bienvenido al juego de adivinar capitales.')
    nombre = str(input('Introduce tu nombre: '))
    edad = 0
    while True:
        try:
            edad = int(input('Introduce tu edad: '))
            break
        except ValueError:
            print('Por favor inserta un numero: ')
    informacion['nombre'] = nombre.capitalize()
    informacion['edad'] = edad
    return informacion

def juego(capitales : dict, jugador: dict):
    #Se coge un elemento aleatorio del diccionario capitales
    pais,capital = choice(list(capitales.items()))
    x = '_'*len(capital)
    letras_mostradas = []
    contador = 1
    while True:
        print('\n¿Cual es la capital de '+str(pais)+'?')
        respuesta = str(input(str(x)+'\n'))
        if respuesta.lower() == capital.lower():
            if contador > 1:
                print('\nHas acertado !!!\n')
                return 'Has acertado la capital de '+str(pais)+' ('+str(capital)+') en '+str(contador)+' intentos'
            else:
                print('\nHas acertado !!!\n')
                return 'Has acertado la capital de '+str(pais)+' ('+str(capital)+') en '+str(contador)+' intento'
        else:
            contador+=1
            while True:
                letraDestapada = randint(0,(len(capital)-1))
                if letraDestapada not in letras_mostradas:
                    x = x[:letraDestapada] +str(capital[letraDestapada])+ x[letraDestapada+1:]
                    letras_mostradas.append(letraDestapada)
                    break
        
def guardarPartida(datosPartida : list , informacionJugador : dict):
    pathC = path + informacionJugador['nombre'] + '.txt'
    filepath = os.path.join(pathC)
    if checkDirectoryPath(path):
        listado = cargarNombresFicheros(path)
        if informacionJugador['nombre'] in listado:
            with open(filepath,'a+',encoding="utf-8") as file:
                file.write('\n')
                file.write(fechaHora())
                file.write('\n\n')
                file.writelines(datosPartida)
        else:
            with open(filepath,'x+',encoding="utf-8") as file:
                file.write(fechaHora())
                file.write('\n\n')
                file.writelines(datosPartida)
    else:
        with open(filepath,'x+',encoding="utf-8") as file:
            file.write(fechaHora())
            file.write('\n\n')
            file.writelines(datosPartida)

def fechaHora():
    fecha = datetime.now()
    return fecha.strftime("%d/%m/%Y %H:%M:%S")

#Funciones de los ficheros
def checkDirectoryPath(path : str):
    if not os.path.exists(path):
        os.makedirs(path)
        return False
    else:
        return True
            
def cargarNombresFicheros(dir : str):
    listadoDirectorio = os.listdir(dir)
    listadoLimpio = []
    for receta in listadoDirectorio:
        x = receta.split('.')
        listadoLimpio.append(x[0])
    return listadoLimpio