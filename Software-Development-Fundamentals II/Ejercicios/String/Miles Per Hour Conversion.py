print('Welcome to the Miles Per Hour Conversion App')

#Get the velocity in miles per huor
miles = float(input('What is your speed in miles per hour: '))

#Change from miles per hour to metters per seconds
conversion = round(miles / 2.237,2)
print('Your speed in meters per second is: '+str(conversion))