#from os import system
from listaHash import ListaHash

tablaHash = []
for i in range(5):
    tablaHash.append(ListaHash())

#Crear un elemento para ejecutar la función Hash
h = ListaHash()

while True:
    #system("clear")
    
    for i in range(5):
        print("ListaHash[" + str(i) + "]  = ", end = "")
        tablaHash[i].recorrer()
        print("")
    
    codigo= int(input("\n\nDigite el código: "))
    nombre= input("Digite el nombre:")
    
    clave = h.funcionHash(codigo)
    tablaHash[clave].insertar(codigo, nombre)
    
    
    continuar = input("\n ¿Desea continuar s/n?: ")
    if continuar =='n' or continuar =='N': break
print("\nEL programa ha finalizado")