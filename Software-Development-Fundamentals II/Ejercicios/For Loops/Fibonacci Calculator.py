print('Welcome to the Fibonacci Calculator App')

#Calculate Fibonnaci
num = int(input('How many digits of the Fibonacci Sequence would you like to compute: '))
Fibonnaci = []
actual = 0
for i in range(num):
    if i==0:
        Fibonnaci.append(i+1)
    elif  i==1:
        Fibonnaci.append(i)
    else:
        Fibonnaci.append(Fibonnaci[i-1]+Fibonnaci[i-2])
print(*Fibonnaci)  

#Calculate golden ratio
print('The corresponding Golden Ratio values are: ')
gold = []
for i in range(num):
    if i==0:
        gold.append(float(i+1.0))
    elif  i==1:
        gold.append(float(i+1.0))
    else:
        ratio = (gold[i-2]%gold[i-1])+(gold[i-2]/gold[i-1])
        gold.append(ratio)     
print(*gold)