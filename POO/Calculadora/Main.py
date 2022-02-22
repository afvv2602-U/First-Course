from Calculadora import CalculadoraBasica, CalculadoraCientifica, CalculadoraSolar


def main():
    print('Bienvenido a la calculadora que deseas hacer: ')
    menu()

def menu(**arg):
    sw = arg.get('sw')
    op = int(input('1.Calculadora Basica (Suma,Resta,Multiplicacion,Division)\n2.Calculadora Cientifica (Exponente,Cambio de signo, Raiz cuadrada, Raiz cubica, Raiz n-esima)\n3.Calculadora Solar (Mostrar bateria, Condiciones luminicas, Tiempo de carga)\n'))
    match(op):
        case(1):
            cc = CalculadoraBasica()
            menuBasic(cc)
        case(2):
            cc = CalculadoraCientifica()
            menuCientifico(cc)
        case(3):
            cc = CalculadoraSolar()
            menuSolar(cc)

def menuBasic(calculadora : CalculadoraBasica):
    op = int(input('¿Que operacion quieres realizar: \n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n'))
    match(op):
        case(1):
            num1 = float(input('Introduce el primer valor:'))
            num2 = float(input('Introduce el segundo valor:'))
            print('La suma de {num1} mas {num2} es: ',calculadora.suma(num1,num2))
        case(2):
            num1 = float(input('Introduce el primer valor:'))
            num2 = float(input('Introduce el segundo valor:'))
            print('La resta de {num1} menos {num2} es: ',calculadora.resta(num1,num2))
        case(3):
            num1 = float(input('Introduce el primer valor:'))
            num2 = float(input('Introduce el segundo valor:'))
            print('La multiplicacion de {num1} por {num2} es: ',calculadora.multiplicacion(num1,num2))
        case(4):
            num1 = float(input('Introduce el primer valor:'))
            num2 = float(input('Introduce el segundo valor:'))
            print('La division de {num1} entre {num2} es: ',calculadora.division(num1,num2))
    menu(sw = True)

def menuCientifico(calculadora : CalculadoraCientifica):
    op = int(input('¿Que operacion quieres realizar: \n1.Exponente\n2.Cambio de signo\n3.Raiz cuadrada\n4.Raiz cubica\n5.Raiz n-esima\n'))
    match(op):
        case(1):
            num1 = float(input('Introduce el valor de la base:'))
            num2 = float(input('Introduce el valor del exponente:'))
            print('El exponente de {num1} elevado a {num2} es: ',calculadora.exponente(num1,num2))
        case(2):
            num1 = float(input('Introduce el valor al que quieres cambiar el signo:'))
            print('El cambio de signo de {num1} es: ',calculadora.cambioDeSigno(num1))
        case(3):
            num1 = float(input('Introduce el radicando de la raiz cuadrada'))
            print('La raiz cuadrade de {num1} es: ',calculadora.raizCuadrada(num1))
        case(4):
            num1 = float(input('Introduce el radicando de la raiz cubica'))
            print('La raiz cubica de {num1} es: ',calculadora.raizCubica(num1))
        case(5):
            num1 = float(input('Introduce el radicando de la raiz:'))
            num2 = float(input('Introduce el indice de la raiz'))
            print('La raiz {num2} de {num1} es: ',calculadora.raizEnesima(num1,num2))
    menu(sw = True)
    

def menuSolar(calculadora : CalculadoraSolar):
    op = int(input('¿Que quieres revisar: \n1.Carga de la bateria\n2.Intensidad luminica\n3.Tiempo de carga\n'))
    match(op):
        case(1):
            print('La carga de la bateria es: ',calculadora.bateria)
        case(2):
            print('La intensidad luminica actual (1-10) es: ',calculadora.intensidad)
        case(3):
            print('El tiempo de carga estimado hasta llegar al maximo es: ',calculadora.tiempoDeCarga())
    menu(sw = True)

if __name__ == '__main__':
    main()