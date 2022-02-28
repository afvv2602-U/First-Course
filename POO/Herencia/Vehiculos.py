class Vehiculo(object):
    def __init__(self,color,num_ruedas,nombre):
        self.color = color
        self.num_ruedas = num_ruedas
        self.nombre = nombre

    def __str__(self):
        return 'Color {0}, Tiene {1} ruedas, se llama {2} '.format(self.color,self.num_ruedas,self.nombre)
        
class Coche(Vehiculo):
    def __init__(self, color, num_ruedas, nombre,velocidad,cilindrada):
        super().__init__(color,num_ruedas,nombre)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + "{0} km/h {1} cc ".format(self.velocidad,self.cilindrada)

class Tanque(Vehiculo):
    def __init__(self, color, num_ruedas, nombre,velocidad,cilindrada,ocupantes):
        super().__init__(color, num_ruedas, nombre)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.ocupantes = ocupantes

    def __str__(self):
        return super().__str__() + '%i km/h %i cc %i ocupantes '%(self.velocidad,self.cilindrada,self.ocupantes)

class Bicicleta(Vehiculo):
    def __init__(self, color, num_ruedas, nombre,tipo,peso):
        super().__init__(color, num_ruedas, nombre)
        self.tipo = tipo
        self.peso = peso
    
    def __str__(self):
        return super().__str__() + ', tipo %s , peso %i '%(self.tipo, self.peso)

class Limusina(Coche):
    def __init__(self, color, num_ruedas, nombre, velocidad, cilindrada,num_asientos,num_puertas):
        super().__init__(color, num_ruedas, nombre, velocidad, cilindrada)
        self.num_asientos = num_asientos
        self.num_puertas = num_puertas

    def __str__(self):
        return super().__str__() + ', numero de asientos %i, numero de puertas %i'%(self.num_asientos,self.num_puertas)

class Camion(Tanque):
    def __init__(self, color, num_ruedas, nombre, velocidad, cilindrada, ocupantes,num_asientos,armas : bool):
        super().__init__(color, num_ruedas, nombre, velocidad, cilindrada, ocupantes)
        self.num_asientos = num_asientos
        self.armas = armas

    def __str__(self):
        return super().__str__() + ', numero de asientos %i, tiene armas %r'%(self.num_asientos,self.armas)


class Triciclo(Bicicleta):
    def __init__(self, color, num_ruedas, nombre, tipo, peso,bocina : bool):
        super().__init__(color, num_ruedas, nombre, tipo, peso)
        self.bocina = bocina

    def __str__(self):
        return super().__str__() + ', tiene bocina %r'%(self.bocina)