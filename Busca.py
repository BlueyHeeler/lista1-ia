from Node import Node

node0 = Node(None, "I")
node1 = Node(None, 1)
node2 = Node(None, 2)
node3 = Node(None, 3)
node4 = Node(None, 4)
node5 = Node(None, 5)
node6 = Node(None, 6)
node7 = Node(None, 7)
node8 = Node(None, 8)
node9 = Node(None, 9)
node10 = Node(None, 10)
node11 = Node(None, 11)
node12 = Node(None, 12)
node13 = Node(None, 13)
node14 = Node(None, 14)
node15 = Node(None, 15)
node16 = Node(None, 16)
node17 = Node(None, 17)
node18 = Node(None, 18)
node19 = Node(None, 19)
node20 = Node(None, 20)
node21 = Node(None, 21)
node22 = Node(None, 22)
node23 = Node(None, 23)


node0.setNext([node1,node2])
node1.setNext([node3,node4])
node3.setNext([node7,node8])
node8.setNext([node13,node14])
node14.setNext([node23])
node4.setNext([node9])
node9.setNext([node15,node16])
node15.setNext([node21])
node16.setNext([node23])
node2.setNext([node5,node6])
node5.setNext([node10])
node10.setNext([node17,node18])
node18.setNext([node22])
node22.setNext([node23])
node6.setNext([node11,node12])
node11.setNext([node19,node20])
node12.setNext([node23])

#elemento que quer ser encontrado
goal = 23

def buscaEmLargura(node):
    print("Busca em Largura") 
    lista = []                              #Utilizado para percorrer
    lista2 = []                             #Utilizado apenas para mostra o que está ocorrendo
    lista3 = []                             #Armazena o caminho feito
    lista4 = []                             #Armazena lista3

    lista.append(node)
    lista2.append(node.nome)

    while True:
        if len(lista) == 0:                  #se a lista estiver vazia parar
            break
        
        current_node = lista[0]
        print(lista2)
        print(current_node.nome)
        
        if current_node.nome == goal:
            print("Achou !!!")
            x = current_node
            while x != None:                #Procedimento que armazena o caminho feito
                lista3.insert(0,x)
                x = x.previous
            lista4.append(lista3)
            lista3 = []
         
        if current_node.next == None:       #caso que testa se o nó não possui próximo elemento
            pass
        else:

            temp = current_node

            for x in temp.next:             #anexa os elementos em fila
                x.previous = current_node   #define o pai
                lista.append(x)
                lista2.append(x.nome)
        lista2.remove(current_node.nome)
        lista.remove(current_node)

    print("Terminou")
    for x in lista4:
        for y in x:
            if y!= None:
                print(y.nome, end=" ")
        print("\n")

def buscaEmProfundidade(node):
    print("Busca em Profundidade") 
    lista = []                              #Utilizado para percorrer
    lista2 = []                             #Utilizado apenas para mostra o que está ocorrendo
    lista3 = []                             #Armazena o caminho feito
    lista4 = []                             #Armazena lista3

    cont = 1

    lista.append(node)
    lista2.append(node.nome) 

    while True:
        if len(lista) == 0:                 #Se o algoritmo percorrer todos os nós
            break

        current_node = lista[0]             #No atual
        print(current_node.nome)
        print(lista2)

        if current_node.nome == goal:       #Verifica se é o elemento procurado
            print("Achou !!!")
            x = current_node
            while x != None:                #Procedimento que armazena o caminho feito
                lista3.insert(0,x)
                x = x.previous
            lista4.append(lista3)
            lista3 = []


        if current_node.next == None:       #Se o próximo nó for vazio
            pass

        else:                               #Se o próximo nó não for vazio
            temp = current_node             #variável temporária

            for x in temp.next:             #anexa os elementos em pilha
                x.previous = current_node   #define o pai dos nós filhos
                lista2.insert(cont,x.nome)
                lista.insert(cont,x)
                cont+=1
            cont = 1
        lista.remove(lista[0])
        lista2.remove(lista2[0])
    
    print("Terminou")
    for x in lista4:
        for y in x:
            if y!= None:
                print(f"{y.nome}", end=" ")
        print("\n")

buscaEmLargura(node0)
print("\n==============================")
buscaEmProfundidade(node0)