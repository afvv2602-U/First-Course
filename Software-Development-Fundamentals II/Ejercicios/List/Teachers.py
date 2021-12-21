print('Welcome to the Favorite Teachers Program')

#Get a list of teachers in order of like
Teachers = []
Teachers.append(str(input('Who is your first favorite teacher: ')).capitalize())
Teachers.append(str(input('Who is your second favorite teacher: ')).capitalize())
Teachers.append(str(input('Who is your thrid favorite teacher: ')).capitalize())
Teachers.append(str(input('Who is your fourth favorite teacher: ')).capitalize())

#Display results
TeachersO = Teachers.copy() 
print('\nYour favorite teachers ranked are: '+str(Teachers))
Teachers.sort()
print('Your favorite teachers aphabetically are: '+str(Teachers))
Teachers.reverse()
print('Your favorite teachers in reverse alphabetical order are: '+str(Teachers))

#Display information from original array
print('\nYour top two teachers are: '+str(TeachersO[0])+ ' and '+str(TeachersO[1]))
print('Your next two favorite teachers are: '+str(TeachersO[2])+ ' and '+str(TeachersO[3]))
print('Your last favorite teacher is: '+str(TeachersO[-1]))
print('You have a total of '+str(len(TeachersO))+' favorite teachers\n')

#Change the first position
TeachersO.insert(0,str(input(('Oops, '+str(TeachersO[0])+' is no longer your first favorite teacher,\nWho is your new FAVORITE teacher: ')).capitalize()))

#Clean the previous list and display the new results
Teachers.clear()
Teachers = TeachersO.copy()
print('\nYour favorite teachers ranked are: '+str(Teachers))
Teachers.sort()
print('Your favorite teachers aphabetically are: '+str(Teachers))
Teachers.reverse()
print('Your favorite teachers in reverse alphabetical order are: '+str(Teachers))

#Display information from updated array
print('\nYour top two teachers are: '+str(TeachersO[0])+ ' and '+str(TeachersO[1]))
print('Your next two favorite teachers are: '+str(TeachersO[2])+ ' and '+str(TeachersO[3]))
print('Your last favorite teacher is: '+str(TeachersO[-1]))
print('You have a total of '+str(len(TeachersO))+' favorite teachers\n')

#Delete one professor
delProf = str(input('You\'ve decided you no longer like a teacher. Which teacher would you like to remove from you list: ')).capitalize()
TeachersO.remove(delProf)

#Clean the previous list and display the new results
Teachers.clear()
Teachers = TeachersO.copy()
print('\nYour favorite teachers ranked are: '+str(Teachers))
Teachers.sort()
print('Your favorite teachers aphabetically are: '+str(Teachers))
Teachers.reverse()
print('Your favorite teachers in reverse alphabetical order are: '+str(Teachers))

#Display information from updated array
print('\nYour top two teachers are: '+str(TeachersO[0])+ ' and '+str(TeachersO[1]))
print('Your next two favorite teachers are: '+str(TeachersO[2])+ ' and '+str(TeachersO[3]))
print('Your last favorite teacher is: '+str(TeachersO[-1]))
print('You have a total of '+str(len(TeachersO))+' favorite teachers\n')