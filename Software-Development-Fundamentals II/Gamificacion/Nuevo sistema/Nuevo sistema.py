import os 

informacion = {'Camara de retina':473827163,'Codigo de acceso':182736451,'Palabra clave':102938476,'Codigo de acceso complejo':192534213,'Puerta sin bloqueo':837461320}

def main():
    #Si el fichero existe no hace nada
    if os.path.isfile('Codigos.txt'):
        pass
    else:
        #Si no existe el fichero se crea en modo escritura
        with open('Codigos.txt','x') as file:
            file.write('Clave \t : \t Valor\n')
            #Y se le añaden todos los valores del diccionario informacion
            for k,v in informacion.items():
                file.write(str(k)+'\t : \t'+str(v)+'\n')
    while True:
        #Creamos un menu para organizar los inputs
        opcion = int(input('1. Añadir codigo\n2. Consultar codigo\n3. Eliminar codigo\n4. Salir\n'))
        match opcion:
            #Opcion insertar un nuevo registro
            case(1):
                with open('Codigos.txt','a+') as file:
                    nombre = str(input('Puerta que quieres añadir: '))
                    codigo = int(input('Codigo de acceso: '))
                    file.write(str(nombre)+'\t : \t'+str(codigo))
            #Opcion consultar registro
            case(2):
                sw = False
                mostrarTodo()
                clInput = str(input('Introduce la clave que quieras buscar: '))
                with open('Codigos.txt','r+') as file:
                    for line in file:
                        spt = line.strip().split(':')
                        clave = str(spt[0]).strip()
                        valor = str(spt[1]).strip()
                        if clave.lower().strip() == clInput.strip().lower():
                            print('Se ha encontrado este resultado:')
                            print(str(clave)+' : '+str(valor)+'\n')
                            sw = True
                            break
                if not sw:
                    print('No se han encontrado registros\n')
            #Opcion eliminar registro
            case(3):
                sw = False
                mostrarTodo()
                clInput = str(input('Introduce la clave que quieras eliminar: '))
                with open('Codigos.txt','r+') as file:
                    localLines = file.readlines()
                    file.seek(0)
                    for line in localLines:
                        spt = line.strip().split(':')
                        clave = str(spt[0]).strip()
                        valor = str(spt[1]).strip()
                        if clave.lower().strip() != clInput.strip().lower():
                            file.write(line)
                        else:
                            print('Eliminando el siguiente registo')
                            print(str(clave)+' : '+str(valor))
                            sw = True
                            break
                        file.truncate()
                if not sw:
                    print('No se han encontrado registros para eliminar\n')
            #Cerrar programa
            case(4):
                break

def mostrarTodo():
    with open('Codigos.txt','r+') as file:
        for line in file:
            spt = line.strip().split(':')
            clave = str(spt[0]).strip()
            if clave.lower() == 'clave':
                pass
            else:
                print(clave)
    print('\n')            
if __name__ == "__main__":
    main()