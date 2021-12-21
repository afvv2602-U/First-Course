#import math
import math

#Introduction
print('Welcome to the Factorial Calculator App')
factorial = int(input('What number would you like to compute the factorial of?: '))
result = 1
list = []

#Create the list of nums and calculate the factorial (My method)
for i in range(factorial,0,-1):
    list.append(i)
    if i == 1:
        list.reverse()
        list.insert(0,str(factorial)+'!')    
        list.insert(1,'=')  
    else:
        list.append('*')  
    result = result*i
print(*list)
#Math method
print('\nHere is the result from the math library: \nThe factorial of '+str(factorial)+' is: '+str(math.factorial(factorial)))

#My method
print('\nHere is the result from my own algorithm: \nThe factorial of '+str(factorial)+' is: '+str(result))

print('\nIt is shown twice that '+str(factorial)+'! = '+str(result)+' (with excitement)')   