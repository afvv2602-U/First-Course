import os

num = int(input('Introduce un numero entre el 1 y el 10: '))

#Conseguimos que el fichero se cree en la ruta especifica donde se encuentra el ejercicio
filepath = os.path.join('E:\Immune\Dev 2\Repositorio\Software-Development-Fundamentals\Gamificacion\La extraña maquina',"tabla-"+str(num)+".txt")
file = open(filepath,'w+')
file.write('Se te mostrara la tabla del numero '+str(num)+'\n')
for i in range(10):
    file.write('\n'+str(num)+' * '+str(i+1)+' = '+str(num*(i+1))+'\n')
file.close()