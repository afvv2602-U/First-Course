print('Welcome to the Letter Counter App')

#Get the name from the user
name = str(input('What is your name: '))
print('Hello '+str(name)+'!')
print('I will count the number of times that a specific letter occurs in a message.')
message = str(input('Please enter a message: '))

#Input the letter and count the times that appers in the sentence
letter = str(input('Which letter would you like to count the occurrences of: ')).lower()
number = message.lower().count(letter)
print(str(name)+', your message has '+str(number)+'\'s in it.')