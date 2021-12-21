from datetime import datetime

shoppingList = ['Meat','Cheese']
print('Welcome to the Grocery List App')
print('Current Date and Time: '+str(datetime.now()))
print('You currently have '+ str(shoppingList[0])+' And '+str(shoppingList[1])+' in your list\n')

'''Set new values in the list'''
for i in range(3):
    shoppingList.append(str(input('Type of food to add to the grocery list: ')))

'''Unsorted and Sorted list'''
print('\nHere is your grocery list: '+str(shoppingList))
shoppingList.sort()
print('Here is your grocery list sorted: ')


'''Deleting items from shopping list'''

print('\nSimulating grocery shopping...\n')

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i].capitalize()

for i in range(3):
    print('Current grocery list: '+str(len(shoppingList))+' items\n'+str(shoppingList))
    food = str(input('What food did you just buy: '))
    print('Removing '+food+' from list...')
    shoppingList.remove(food.capitalize())

print('\nCurrent grocery list: '+str(len(shoppingList))+' items\n'+str(shoppingList))

'''Deleting the last index of the list'''

print('Sorry, the store is out of '+str(shoppingList[len(shoppingList)-1])+'.\n')
del(shoppingList[len(shoppingList)-1])
food = str(input('What food would you like instead: ')).capitalize()
shoppingList.append(food)
print('Here is what remains on your grocery list: '+str(shoppingList))