import random as r

tickets_sold = []

def main():
    print('--------------------Power-Ball Simulator--------------------')
    white_balls = int(input('How many white-balls to draw from for the 5 winning numbers (Normally 69): '))
    if white_balls < 6:
        white_balls = 6
    red_balls = int(input('How many red-balls to draw from for the Power-Ball (Normally 26): '))
    if red_balls < 1:
        red_balls = 1
    print('You have 1 in a',calculatePercentage(white_balls,red_balls),' of win this lottery')
    tickets = int(input('Purchase  tickets in what interval: '))
    powerBall(white_balls,red_balls,tickets)
    
def calculatePercentage(white_balls : int ,red_balls : int):
    return ((white_balls)*(white_balls-1)*(white_balls-2)*(white_balls-3)*(white_balls-4))*(red_balls/120)

def powerBall(white_balls: int, red_balls: int ,tickets : int):
    print('\n\n---------Welcome to the Power-Ball-----------\n')
    winning_numbers = generateNums(white_balls,red_balls)
    print('\nTonight\'s winning numbers are:',*winning_numbers)
    input('Press \'Enter\' to begin purchasing tickets!!!')
    buyTickets(tickets,winning_numbers,white_balls,red_balls)

def generateNums(white_balls: int,red_balls: int):
    cont = 1
    numbers = []
    while cont <= white_balls-1:
        num = r.randint(1,white_balls)
        if num not in numbers:
            numbers.append(num)
            numbers.sort()
            cont+=1
        else:
            pass
    powerBall = r.randint(1,red_balls)
    numbers.append(powerBall)
    return numbers

def buyTickets(tickets: int,winning_numbers : list,white_balls : int, red_balls: int ):
    sw = True
    sw = generateTickets(tickets,white_balls,red_balls,winning_numbers)
    while sw:
        op = str(input('Keep purchasing tickets (y/n): '))
        if op[0].lower() == 'y':
            sw = generateTickets(tickets,white_balls,red_balls,winning_numbers)
            pass
        else:
            print('You bought ',len(tickets_sold),' tickets and still lost!\nBetter luck next time!')
            break

def generateTickets(tickets: int,white_balls : int, red_balls: int,winning_numbers: list):
    cont = 0
    while cont<tickets:
        ticket = generateNums(white_balls,red_balls)
        if ticket == winning_numbers:
            print('Winning ticket numbers: ',*ticket)
            print('Purchase a total of ',len(tickets_sold),' tickets.')
            return False
        elif ticket in tickets_sold:
            print('Losing ticket generated; disregard...')
            pass
        else:
            tickets_sold.append(ticket)
            print(*ticket)
            cont+=1
    return True

if __name__ == '__main__':
    main()