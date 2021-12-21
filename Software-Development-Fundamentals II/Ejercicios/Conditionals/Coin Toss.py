from random import randint

def main():
    print('Welcome to the Coin Toss App\n')
    print('I will flip a coin a set number of times.')
    flips = int(input('How many times would you like me to flip the coin: '))
    results = {'heads':0,'tails':0}
    choice = str(input('Would you like to see the result of each flip (y/n): '))
    flipCoin(flips,results,choice[0])
    showResults(results,flips)

#Simulate the coin flipping
def flipCoin(flips,results,choice):
    print('\nFlipping!!!\n')
    #If choice is 'Y'
    if choice.lower() == 'y':
       for i in range(flips):
           if i>0 and results['heads']==results['tails']:
            print('At '+str(i)+' flips, the number of heads and tails were equal at '+str(results['tails'])+' each.\n')    
           coin = randint(0,1)
           if coin == 0:
            print('HEAD')
            results['heads'] += 1
           else:
            print('TAIL')
            results['tails'] += 1  
    #If choice is 'N'
    elif choice.lower() == 'n':
        for i in range(flips):
           if i>0 and results['heads']==results['tails']:
            print('At '+str(i)+' flips, the number of heads and tails were equal at '+str(results['tails'])+' each.')
           coin = randint(0,1) 
           if coin == 0:
            results['heads'] += 1
           else:
            results['tails'] += 1   
    

#Show and calculate the percentage of each option
def showResults(results,flips):
    headPercentage = round((results['heads']*100)/flips,2)
    tailPercentage = round((results['tails']*100)/flips,2)
    print('\nResults Of Flipping A Coin '+str(flips)+' Times:\n')
    print('Side\t\tCount\t\tPercentage')
    print('Heads\t\t'+str(results['heads'])+'/'+str(flips)+'\t\t'+str(headPercentage))
    print('Tails\t\t'+str(results['tails'])+'/'+str(flips)+'\t\t'+str(tailPercentage))


if __name__ == "__main__":
    main()
        
