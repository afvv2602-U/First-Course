# import complex math module  
import cmath  

#Introduction
print('Welcome to the Quadratic Equation Solver App.')
print('A quadratic equation is of the form ax^2 + bx + c = 0\nYour solutions can be real or complex numbers.\nA complex number has two parts: a + bj\nWhere a is the real portion and bj is the imaginary portion.')

#Input
equations = int(input('How many equations would you like to solve today: '))

#Resolve equations
for i in range(1,equations+1):
    print('Solving equation #'+str(i)+'\n---------------------------------------------------------------')
    a = float(input('Please enter your value of a (coefficient of x^2): '))
    b = float(input('Please enter your value of b (coefficient of x): '))
    c = float(input('Please enter your value of c (coefficient): '))

    #Calculate the discriminant  
    d = (b**2) - (4*a*c)  

    #Calculate solutions
    x1 = (-b-cmath.sqrt(d))/(2*a)  
    x2 = (-b+cmath.sqrt(d))/(2*a) 

    #Print results 
    print('\nThe solutions to '+str(a)+'x^2 + '+str(b)+'x + '+str(c)+' = 0 are: ')
    print('x1 = '+str(x1)+'\nx2 = '+str(x2))
    
