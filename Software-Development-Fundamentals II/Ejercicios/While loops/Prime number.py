import time as t

def main():
    print('Welcome to the Prime Number App')
    while True:
        op = int(input('\nEnter 1 to determine if a specific number is prime\2Enter 2 to determine all prime numbers within a set range.\nEnter your choice 1 or 2:'))
        if op == 1:
            num = int(input('\nEnter a number to determine if its is prime or not: '))
            sw = prime(num)
            if sw:
                print(str(num),'is prime!')
            else:
                print(str(num),'is not prime!')
        else:
            primeList()
        op = str(input('Would you like to run the program again (y/n): '))
        if op[0].lower() == 'y':
            pass
        else:
            print('Thank you for using the program. Goodbye!.')
            break

def prime(num : int):
    sw = True
    for i in range(num,1,-1):
        if i == num or i == 0:
            pass
        elif num%i == 0:
            sw = False    
            break
    return sw

def primeList():
    lower = int(input('Enter the lower bound of your range: '))
    upper = int(input('Enter the upper bound of your range: '))
    primeNums = []
    #Count time
    start_time = t.time()
    for i in range(lower,upper,1):
        if prime(i):
            primeNums.append(i)
    print("\nCalculations took a total of %1.4f seconds" % (t.time() - start_time))
    print('The following numbers beetween ',str(lower),' and ',str(upper),' are prime: ')
    input("Press Enter to continue...")
    print(*primeNums,sep='\n')

if __name__ == '__main__':
    main()