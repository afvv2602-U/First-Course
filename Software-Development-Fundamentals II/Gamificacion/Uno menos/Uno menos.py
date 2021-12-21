#El tiempo que tarda cada puerta en abrirse
puertasT = {'Cámara de retina':40,'Código de acceso':50,'Palabra clave':30,'Código de acceso complejo':70,'Puerta sin bloqueo':0}

#Zonas
zonas = {'Zona 1': {'Cámara de retina':3,'Palabra clave':1}
,'Zona 2': {'Puerta sin bloqueo':2,'Código de acceso':5}
,'Zona 3': {'Puerta sin bloqueo':5,'Cámara de retina':1}
,'Zona 4': {'Código de acceso':2,'Palabra clave':4}}

#Total de puertas
contadorPuertas = {'Cámara de retina':0,'Código de acceso':0,'Palabra clave':0,'Código de acceso complejo':0,'Puerta sin bloqueo':0}

#Un bucle coge las keys del diccionario zonas
for keys in zonas:
    #Y con esas keys entramos en el otro diccionario cogiendo la k las keys y v cogiendo los valores de las mismas
    for k,v in zonas.get(keys).items():
        #Sumamos la cantidad de puertas
        contadorPuertas[k] += v
print('El total de puertas es:\n')
for key in contadorPuertas:
  print(str(key)+ " : "+str( contadorPuertas[key]))

#Zona 2
contZona2 = 0
for keys in zonas:
    if keys == 'Zona 2':
        for k,v in zonas.get(keys).items():
            contZona2 += v
print('\nEn la zona dos hay un total de: '+str(contZona2)+' puertas')

#Zona 1
contZona1 = 0
for keys in zonas:
    if keys == 'Zona 1':
        for k,v in zonas.get(keys).items():
            if k == 'Palabra clave':
                contZona1 += v
print('\nEn la zona dos hay un total de: '+str(contZona1)+' puertas con palabra clave')

#Tiempo de las zonas
contadorTiempo = {'Zona 1': 0,'Zona 2': 0,'Zona 3': 0,'Zona 4': 0}
for keys in zonas:
    for k,v in zonas.get(keys).items():
        contadorTiempo[keys] += (puertasT[k]*v)

print('\nEl tiempo total de cada zona es\n')
for key in contadorTiempo:
  print(str(key)+ " : "+str(contadorTiempo[key])+' minutos')

