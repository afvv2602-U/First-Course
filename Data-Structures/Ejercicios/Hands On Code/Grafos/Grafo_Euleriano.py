#Programa que crea un grafo y lo devuelve en formato pdf
from graphviz import Graph as gr

grafo = gr('G', filename = 'eureliano.gv', engine='circo') # Engine es el motor grafico
aristas = int(input('Cantidad de aristas que tiene tu grafo: '))

def euler(pdf):
    visitados = [] #Cantidad de nodos visitados
    cola = []
    ciclos = 0
    ContadorNodosAgregados = 0
    caminos = 0
    acumulador = 0 # Cuenta la cantidad de veces que se ha pasado por un vertice
    nodos_pares = 0

    for nodoinicial in range(aristas):
        nodoinicial = str(input('Inserte nombre para el nodo inicial: '))
        grafo.attr('node', shape='doublecircle')
        #Funcion que crea los nodos por separado graficamente
        grafo.node(nodoinicial)

        nodo_llegada = str(input('Nombre un nodo para conectarlo con el anterior: '))
        #Funcion que contecta los nodos de acuerdo a la decision del usuario
        grafo.edge(nodoinicial,nodo_llegada) #edge = arista

        #Condicion que guarda en nuestro array cola cada nodo ingresado en nuestra variable nodoinicial
        if(aristas>=1):
            cola.append(nodoinicial)
            ContadorNodosAgregados +=1

        #Doble ciclo for para conseguir los ciclos eulerianos de nuestro grafo
        for indice in range(len(cola)):
            actual = cola[indice]
            for j in range(len(cola)):
                if actual == cola[j]:
                    nodos_pares +=1
        if nodos_pares >= len(cola):
            caminos+=1

        #Ciclo for para conseguir los caminos euleiranos de nuestro grafo
        for elementos in range(len(cola)):
            if (cola[elementos] == nodo_llegada or nodoinicial):
                acumulador += 1

        if acumulador >= len(cola):
            caminos += 1

        visitados.append(ContadorNodosAgregados)
        grafo.attr(label = r'\n\nGrafo Euleriano\n', fontsize = '12')
        grafo.view()

        print('Los elementos de la cola son los nodos:', cola)
        print('La cantidad de nodos visitados es de:', visitados)
        print('La cantidad de ciclos encontrados es de:', ciclos)
        print('La cantidad de caminos encontrados es de:', caminos)

print(euler(grafo))