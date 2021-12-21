from random import randint

def main():
    print('Welcome to a game of Rock, Paper, Scissors')
    name = str(input('Hello! What is your name: '))
    rounds = int(input('How many round would you like to play: '))
    game(rounds,name)

def game(rounds,name):
    moves = ['rock','paper','scissors']
    cont = {name:0,'computer':0}
    for i in range(rounds):
        print('Round '+str(i+1))
        print(str(name)+': '+str(cont[name])+'\t\tComputer: '+str(cont['computer']))
        choice = str(input('Time to pick...rock,paper,scissors: ')).lower()
        if choice in moves:
            computerChoice = randint(0,2)
            print('Computer: '+str(moves[computerChoice]))
            print(str(name)+': '+str(choice))
            if choice == moves[computerChoice]:
                print('It is a tie, how boring!')
            else:
               cont = checkResults(choice,moves[computerChoice],cont,name,i)
        else:
            print('That is not a valid game option!\nComputer gets the point!')
            cont['computer']+=1
    print('Final Game Results')
    print('Rounds Played: '+str(rounds))
    print('Player Score: '+str(cont[name]))
    print('Computer Score: '+str(cont['computer']))
    if cont[name] > cont['computer']:
        print(str(name)+' Won')
    elif cont[name] == cont['computer']:
        print('Theres no winner TIE')
    else:
        print('Computer Won')


def checkResults(choice,computerChoice,cont,name,i):
    match(choice):
        case ('paper'):
            if computerChoice == 'rock':
                print('Paper covers rock!')
                print('You won round '+str(i+1))
                cont[name]+=1
            elif computerChoice == 'scissors':
                print('Scissors cut paper!')
                print('Computer won round '+str(i+1))
                cont['computer']+=1
        case('scissors'):
            if computerChoice == 'rock':
                print('rock smashes scissors!')
                print('Computer won round '+str(i+1))
                cont['computer']+=1
            elif computerChoice == 'paper':
                print('Scissors cut paper!')
                print('You won round '+str(i+1))
                cont[name]+=1
        case('rock'):
            if computerChoice == 'paper':
                print('Paper covers rock!')
                print('Computer won round '+str(i+1))
                cont['computer']+= 1
            elif computerChoice == 'scissors':
                print('rock smashes scissors!')
                print('You won round '+str(i+1))
                cont[name]+=1    
    return cont

    	
if __name__ == "__main__":
    main()
        