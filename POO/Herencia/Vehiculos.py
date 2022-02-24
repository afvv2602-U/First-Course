class Vehiculo(object):
    def __init__(this,color,num_ruedas,nombre):
        this.color = color
        this.num_ruedas = num_ruedas
        this.nombre = nombre

    def __str__(this):
        return 'Color {0}, Tiene {1} ruedas, se llama {2} '.format(this.color,this.num_ruedas,this.nombre)
        
class Coche(Vehiculo):
    def __init__(this, color, num_ruedas, nombre,velocidad,cilindrada):
        super().__init__(color,num_ruedas,nombre)
        this.velocidad = velocidad
        this.cilindrada = cilindrada

    def __str__(this):
        return super().__str__() + "{0} km/h {1} cc ".format(this.velocidad,this.cilindrada)

class Tanque(Vehiculo):
    def __init__(this, color, num_ruedas, nombre,velocidad,cilindrada,ocupantes):
        super().__init__(color, num_ruedas, nombre)
        this.velocidad = velocidad
        this.cilindrada = cilindrada
        this.ocupantes = ocupantes

    def __str__(this):
        return super().__str__() + '%i km/h %i cc %i ocupantes '%(this.velocidad,this.cilindrada,this.ocupantes)

class Bicicleta(Vehiculo):
    def __init__(this, color, num_ruedas, nombre,tipo,peso):
        super().__init__(color, num_ruedas, nombre)
        this.tipo = tipo
        this.peso = peso
    
    def __str__(this):
        return super().__str__() + ', tipo %s , peso %i '%(this.tipo, this.peso)

class Limusina(Coche):
    def __init__(this, color, num_ruedas, nombre, velocidad, cilindrada,num_asientos,num_puertas):
        super().__init__(color, num_ruedas, nombre, velocidad, cilindrada)
        this.num_asientos = num_asientos
        this.num_puertas = num_puertas

    def __str__(this):
        return super().__str__() + ', numero de asientos %i, numero de puertas %i'%(this.num_asientos,this.num_puertas)

class Camion(Tanque):
    def __init__(this, color, num_ruedas, nombre, velocidad, cilindrada, ocupantes,num_asientos,armas : bool):
        super().__init__(color, num_ruedas, nombre, velocidad, cilindrada, ocupantes)
        this.num_asientos = num_asientos
        this.armas = armas

    def __str__(this):
        return super().__str__() + ', numero de asientos %i, tiene armas %r'%(this.num_asientos,this.armas)


class Triciclo(Bicicleta):
    def __init__(this, color, num_ruedas, nombre, tipo, peso,bocina : bool):
        super().__init__(color, num_ruedas, nombre, tipo, peso)
        this.bocina = bocina

    def __str__(this):
        return super().__str__() + ', tiene bocina %r'%(this.bocina)