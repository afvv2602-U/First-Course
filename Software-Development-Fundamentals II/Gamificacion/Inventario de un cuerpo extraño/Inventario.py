import os 

num = int(input('Introduce un numero del 1 al 10 para mostrar esa tabla de multiplicar: '))

try:
    filepath = os.path.join('E:\Immune\Dev 2\Repositorio\Software-Development-Fundamentals\Gamificacion\Inventario de un cuerpo extraño','tabla-'+str(num)+'.txt')
    with open(filepath,'r') as f:
        for row in f:
            print(row.rstrip())
except IOError:
    print('El fichero no existe')


# Creacion de un fichero con todas las tablas de multiplicar del 1 al 10

# filepath = os.path.join('E:\Immune\Dev 2\Repositorio\Software-Development-Fundamentals\Gamificacion\Inventario de un cuerpo extraño',"tablas de multiplicar"+".txt")
# file = open(filepath, 'w+')
# file.write('Se te mostrara la tablas de multiplicar del 1 al 10 \n')
# for i in range(10):
#     file.write('\nTabla del '+str(i+1)+'\n')
#     for j in range(10):
#         file.write((str(i+1)+' * '+str(j+1)+' = '+str((j+1)*(i+1))+'\n'))
# file.close()