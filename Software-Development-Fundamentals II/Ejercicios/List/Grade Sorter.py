print('Welcome to the Grade Sorter App')

'''Get inputs from user'''
grades = []
for i in range(4):
    grades.append(int(input('What is your '+str(i+1)+'° note (0-100): ')))

print('Your grades are: '+str(grades))

'''Sorting array'''
grades.sort(reverse=True)
print('Your grades from highest to lowest are: '+str(grades)+
'\nThe lowest two grades will now be dropped.'
'\nRemoved grade: '+str(grades[2])+
'\nRemoved grade: '+str(grades[3]))

'''Removed last two grades'''

del grades[2:4]
print('Your remaining grades are: '+str(grades))
print('Nice work! Your highest grade is: '+str(grades[0]))