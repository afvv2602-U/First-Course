from random import choice , randint

def main():
    print('Welcome to the Guess My Word App')
    while True:
        game()
        op = str(input('Would you like to run the program again (y/n): '))
        if op[0].lower() == 'y':
            pass
        else:
            print('Thank you for playing our game!.')
            break

def game():
    category,listX = getList()
    word = choice(listX)
    #Se coge un elemento aleatorio del diccionario diccionario
    x = '_'*len(word)
    chars_displayed = []
    cont = 1
    print('\nGuess a ',str(len(word)),' letter word from the following category: ',str(category))
    while True:
        respuesta = str(input(str(x)+'\n\nEnter your guess: '))
        if respuesta.lower() == word.lower():
            if cont > 1:
                print('\nCorrect! You guessed the word in 1 guess !!!\n')
                break
            else:
                print('\nCorrect! You guessed the word in ',cont,' guesses !!!\n')
                break
        else:
            print('That is not correct. Let us reveal a letter to help you!')
            cont+=1
            while True:
                new_char_display = randint(0,(len(word)-1))
                if new_char_display not in chars_displayed:
                    x = x[:new_char_display] +str(word[new_char_display])+ x[new_char_display+1:]
                    chars_displayed.append(new_char_display)
                    break
  
def getList():
    game = {'capitals':['Buenos Aires','Yerevan','Vienna','Athens'],
    'biology':['Prokaryotic','Cell','Chloroplast','Diastole'],
    'history':['Operation Barbarossa','Stalingrad','Siege of Leningrad','Brusilov'],
    'films':['Parasite','Pulp Fiction','GoodFellas','Titanic','Inception'],
    'videogames':['GTA 5','Zelda','Bioshock','Minecraft','Final Fantasy','Tekken']}
    category,word = choice(list(game.items()))
    return category,word

if __name__ == '__main__':
    main()