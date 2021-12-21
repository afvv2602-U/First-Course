from random import randint

#Main function
def main():
    print('Welcome to the Python Dice App')
    while True:
        roll_dice(dice_sides(), dice_number())
        if input('Would you like to roll again (y/n): ').strip().lower() == 'y':
            pass
        else:
            print('Thank you for using the Python Dice App.')
            break
       
def dice_sides():
    return int(input('\nHow many sides would you like on your dice: '))
    
def dice_number():
    return int(input('How many dice would you like to roll: '))

def roll_dice(sides,rolls):
    print('\nYou rolled '+str(rolls)+' '+str(sides)+' sided dice')
    dice = []
    for i in range(rolls):
        #Generate random int between 1 and sides of the dice
        dice.append(randint(1,sides))
    print('\n-----Results are as followed-----\n')
    total = 0
    for num in dice:
        total += num
        #Print every number in dice
        print(num)
    print('\nThe total value of your roll is '+str(total))


if __name__ == "__main__":
    main()