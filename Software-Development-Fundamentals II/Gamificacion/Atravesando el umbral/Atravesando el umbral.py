numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros)):
    match(i):
        case 4:
            numeros[i] = numeros[i]*2
        case 7:
            numeros[i] = numeros[i]*2
        case 9:
            numeros[i] = numeros[i]*2
print(*numeros)