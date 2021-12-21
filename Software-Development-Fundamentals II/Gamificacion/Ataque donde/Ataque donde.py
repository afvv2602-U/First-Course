cadena = "Sala Hipersueño"

#First two characters
print(cadena[0:2])

#Last three characters
print(cadena[-3:])

#Print cadena step by 2
for i in range(len(cadena)):
    if i%2 == 0:
        pass
    else:
        print(cadena[i],end=' ')

print('\n'+str(cadena)+' '+str(cadena[::-1]))