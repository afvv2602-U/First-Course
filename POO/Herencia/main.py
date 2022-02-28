from Vehiculos import Vehiculo,Coche,Tanque,Bicicleta,Limusina,Camion,Triciclo

def main():
    vehiculos = creacionObjetos()
    for actual in vehiculos:
        #Visualizamos los datos de los objetos creados
        print(actual.__str__())
    

def creacionObjetos():
    vehiculos = []
    vehiculo = Vehiculo('Rojo','4','Quad')
    coche = Coche('Azul','4','e36',200,120)
    tanque = Tanque('Verde','14','M1 Abrams',67,1500,4)
    bicicleta = Bicicleta('Dorada y negra','2','Street Cryis','Street BMX',9)
    limusina = Limusina('Rosa','6','Jeep Wrangler',140,400,22,6)
    camion = Camion ('Verde','6','Mercedes-Benz Zetros',200,598,20,20,False)
    triciclo = Triciclo('Rojo','3','Invictus','Electrico',100,True)
    vehiculos.append(vehiculo)
    vehiculos.append(coche)
    vehiculos.append(tanque)
    vehiculos.append(bicicleta)
    vehiculos.append(limusina)
    vehiculos.append(camion)
    vehiculos.append(triciclo)
    return vehiculos

if __name__ == '__main__':
    main()