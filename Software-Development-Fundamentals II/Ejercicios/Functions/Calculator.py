#Define a global variable
summary = []

def main():
    print('Welcome to The Python Calculator App\nEnter two numbers and an operation and the desired operation will be performed.')
    while True:
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter a number: '))
        choice = str(input('Enter an operation (addition, subtraction, multiplication, division, or exponentiation):'))
        match choice[0].lower().strip():
            case('a'):
                add(num1,num2)
            case('s'):
                subtract(num1,num2)
            case('m'):
                multiply(num1,num2)
            case('d'):
                divide(num1,num2)
            case('e'):
                exponent(num1,num2)
            case _:
                print('Invalid Operation')
        if str(input('Would you like to run the program again (y/n): ')).strip().lower() != 'y':
            print('Calculation summary\n')
            #Display all the content in summary
            for line in summary:
                print(line)
            break

#Calculator functions
def add(num1,num2):
    summary.append(str(str(num1) +' + '+str(num2)+' = '+str(num1+num2)))
    print('The sum of '+str(num1)+' and '+str(num2)+' is '+str(num1+num2))
    return round((num1+num2),4)    

def subtract(num1,num2):
    summary.append(str(str(num1) +' - '+str(num2)+' = '+str(num1-num2)))
    print('The difference of '+str(num1)+' and '+str(num2)+' is '+str(num1-num2))
    return round((num1-num2),4)  

def multiply(num1,num2):
    summary.append(str(str(num1) +' * '+str(num2)+' = '+str(num1*num2)))
    print('The product of '+str(num1)+' and '+str(num2)+' is '+str(num1*num2))
    return round((num1*num2),4)  

def divide(num1,num2):
    if num2 != 0:
        summary.append(str(str(num1) +' / '+str(num2)+' = '+str(num1/num2)))
        print('The quotient of '+str(num1)+' and '+str(num2)+' is '+str(num1/num2))
        return round((num1/num2),4)  
    else:
        summary.append('DIV ERROR')
        return print('DIV ERROR')

def exponent(num1,num2):
        summary.append(str(str(num1) +' ** '+str(num2)+' = '+str(num1**num2)))
        print('The result of '+str(num1)+' raised to the '+str(num2)+' power is '+str(num1**num2))
        return round((num1**num2),4)  

if __name__ == "__main__":
    main()