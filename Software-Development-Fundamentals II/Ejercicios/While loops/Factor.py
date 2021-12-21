def main():
    print('Welcome to the Factor Generator App')
    num = int(input('Enter a number to determine all factors of that number: '))
    while True:
        factor(num)
        op = str(input('Run again (y/n): '))
        if op[0].lower() == 'y':
            pass
        else:
            print('Thank you for using the program. Have a great day!.')
            break
                       
def factor(num : int):
    factors = {}
    print('Factors of ',str(num),' are:\n')
    for i in range(1,num+1):
        if  num % i == 0:
            factors[i] = num/i
    #Mostramos solo las claves
    for k,v in factors.items():
        print(k)
    #Resumen de todos los factores
    print('\nIn summary: ')
    for k,v in factors.items():
        print(str(k),' * ',str(v),' = ',str(k*v))


if __name__ == '__main__':
    main()