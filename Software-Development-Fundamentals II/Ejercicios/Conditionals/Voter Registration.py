from typing import ChainMap


def main():
    list = ['Republican','Democratic','Independent','Libertarian','Green']
    print('Welcome to the Voter Registration App')
    name = str(input('Please enter your name: '))
    age = int(input('Please enter your age: '))
    if age >20:
        print('Congratulations '+str(name)+' You are old enough to register to vote.')    
        print(*list,sep='\n')
        choice = str(input('What party would you like to join: '))
        if choice.capitalize() in list:
            print('Congratulations '+str(name)+' You have joined the '+str(choice.capitalize())+' party!')
            if choice.capitalize() == 'Republican':
                print('That is a major party')
            elif choice.capitalize() == 'Independent':
                print('You are an independent person!') 
        else:
            print('Please enter a partie on the list')
    else:
        print('You are not old enough to register to vote')


if __name__ == "__main__":
    main()
        