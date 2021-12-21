print('Welcome to the Temperature Conversion App')

#Get temperate from user in fahrenheit
fahrenheit = float(input('What is the given temperature in degrees Fahrenheit: '))

#Conversions
celsius = round( (fahrenheit - 32) * 5/9,4)
kelvin = round(((fahrenheit - 32) * 5/9 + 273.15),4)

#Display results
print('Degrees Fahrenheit: '+str(fahrenheit)+'\nDegrees Celsius: '+str(celsius)+'\nDegrees Kelvin: '+str(kelvin))