from random import randint

print('Welcome to the Guess My Number App')
name = str(input('Hello! What is your name: '))
print('Well '+str(name)+', I am thinking of a number between 1 and 20')
num = randint(1,20)
sw = False
for i in range(5):
    guess = int(input('Take a guess: '))
    if guess > num:
        print('Your guess is too high')
    elif guess == num:
        print('Good job, '+str(name)+'! You guessed my number in '+str(i+1)+' guesses!')
        sw = True
        break
    else:
        print('Your guess is too low')
if sw == False:
    print('Game Over. The number I was thinking of was '+str(num)+'.')