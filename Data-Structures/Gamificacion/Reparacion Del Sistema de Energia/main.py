def main():
    gadgets = ['Bateria','Portatil',100,'Ordenador Central',310.28,'Altavoces'
    ,27.00,'Pantalla',1000,'Maletin Electronico','Lente de camara']
    strings = []
    nums = []
    for item in gadgets:
        if isinstance(item,str):
            strings.append(item)
        elif isinstance(item,int) or isinstance(item, float):
            nums.append(item)
    #Ordenar descendente
    strings.sort()
    nums.sort()
    print(*strings)
    print(*nums)
    #Reverso
    strings.reverse()
    nums.reverse()
    print(*strings)
    print(*nums)
    

if __name__ == '__main__':
    main()