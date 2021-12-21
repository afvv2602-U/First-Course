def main():
    print('Welcome to the Even Odd Number Sorter App\n')
    nums = str(input('Enter a string of numbers separated by a comma (,): '))
    while True:
        evenOdd(nums)
        op = str(input('Would you like to run the program again (y/n): '))
        if op[0].lower() == 'y':
            pass
        else:
            print('Thank you for using the program. Goodbye!.')
            break

def evenOdd(nums : str):
    numsSplited = nums.split(',')
    odd = []
    even = []
    #summary
    print('\n-----Result Summary-----')
    for number in numsSplited:
        if int(number)%2 == 0:
            print(str(number),'is even!')
            even.append(number)
        else:
            print(str(number),'is odd!')
            odd.append(number)
    #Even
    print('\nThe following ',len(even),' numbers are even: ')
    print(*even,sep='\n')
    #Odd
    print('\nThe following ',len(odd),' numbers are odd: ')
    print(*odd,sep='\n')


if __name__ == '__main__':
    main()