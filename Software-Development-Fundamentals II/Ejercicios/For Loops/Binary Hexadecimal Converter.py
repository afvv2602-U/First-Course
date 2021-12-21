print('Welcome to the Binary/Hexadecimal Converter App')

#Get the input
list = int(input('Compute binary and hexadecimal values up to the following decimal number: '))
print('Generating lists....complete!')

#Get two nums from user
print('Using slices, we will now show a portion of each list.')
startNum = int(input('What decimal number would you like to start at: '))
stopNum = int(input('What decimal number would you like to stop at: '))

#Print decimal values between 'startNum' and 'stopNum'
print('Decimal values from '+str(startNum)+' to '+str(stopNum))
for i in range(startNum,stopNum):
    print(i)

#Print binary values between 'startNum' and 'stopNum'
print('Binary values from '+str(startNum)+' to '+str(stopNum))
for i in range(startNum,stopNum):
    print(bin(i))

#Print hexadecimal values between 'startNum' and 'stopNum'
print('Hexadecimal values from '+str(startNum)+' to '+str(stopNum))
for i in range(startNum,stopNum):
    print(hex(i))

#Print values from 1 to 'list' Decimal --- Binary ---- Hexadecimal
input('Press Enter to see all values from 1 '+str(list)+'.')
print('Decimal----Binary----Hexadecimal \n----------------------------------------------------------')
for i in range(1,list+1):
    print(str(i)+'----'+str(bin(i))+'----'+str(hex(i)))