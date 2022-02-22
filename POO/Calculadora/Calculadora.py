from cmath import sqrt
from random import randint

class Calculadora(object):
    def __init__(this,**arg):
        this.primerValor = arg.get('a')
        this.segundoValor = arg.get('b')
        this.arrayDeValores = arg.get('c')

class CalculadoraBasica(Calculadora):
    def suma(num1 : float , num2: float):
        return num1 + num2

    def resta(num1 : float , num2: float):
        return num1 - num2

    def multiplicacion(num1 : float , num2: float):
        return num1 * num2
    
    def division(num1 : float , num2: float):
        return num1 / num2

class CalculadoraCientifica(Calculadora):
    def exponente(num1 : float,num2: float):
        return pow(num1, num2)

    def cambioDeSigno(num1 : float):
        if num1 < 0:
            return num1.__abs__()
        else:
            return num1 - (num1 ** 2)

    def raizCuadrada(num1 : float):
        return sqrt(num1)

    def raizCubica(num1 : float):
        return pow(num1, 1/3)

    def raizEnesima(num1 : float , raiz : float):
        return pow(num1, 1./raiz)

class CalculadoraSolar(Calculadora):
    def __init__(this):
        this.bateria = randint(0,100)
        this.intensidad = randint(0,10)

    def tiempoDeCarga(this):
        return this.intensidad * (1/this.bateria)
