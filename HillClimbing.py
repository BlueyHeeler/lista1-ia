from Node import Node
nodeS = Node(11,"S")
nodeA = Node(10.4,"A")
nodeB = Node(6.7,"B")
nodeC = Node(4,"C")
nodeD = Node(8.9,"D")
nodeE = Node(6.9,"E")
nodeF = Node(3,"F")
nodeG = Node(None,"G")

nodeS.setNext([nodeA,nodeD])
nodeA.setNext([nodeD,nodeB])
nodeD.setNext([nodeA,nodeE])
nodeB.setNext([nodeC,nodeE])
nodeE.setNext([nodeB,nodeF])
nodeF.setNext([nodeG])

goal = "G"

def HillClimbing(node):
    lista = []                                                                          #utilizado para percorrer
    lista2 = []                                                                         #visitados                 

    lista.append(node)
    for x in range(10):
        
        if len(lista) == 0:                                                             #caso a lista fique vazia
            print("não foi encontrado") 
            break

        current_node = lista[0]                                                         #nó atual
        lista2.append(current_node)                                                     #lista que guarda os nós já visitados
        print(f"nó atual {current_node.nome}")

        if current_node.nome == goal:                                                   #caso o nó atual seja o nó alvo
            print("Achou !!!")
            y = current_node
            while y != None:                                                             #Procedimento que imprime o caminho percorrido
                print(y.nome)
                y = y.previous
            break
        if current_node.next == None:                                                   #caso o próximo nó não exista
            lista.remove(current_node)                                                  #remove da lista o nó atual
            
        else:                                                                           #caso haja um próximo nó
            lista.remove(current_node)                                                  #remove da lista o nó atual
            sorted_nodes = sorted(current_node.next, key=lambda node: node.data)        #ordena a sublista do próximo nó

            cont = 0                   
            for x in sorted_nodes:                                                      #procedimento que adiciona os elementos da sublista ordenada na lista e define o antecessor de um nó
                if x in lista:                                                          #se o elemento já estiver na lista não é permitido adicioná-lo novamente
                    pass        
                else:                                                                   #caso contrário o adicione
                    if x in lista2:                                                     #se o elemento já foi visitado fazer nada
                        pass
                    else:
                        x.previous = current_node                                       #caso contrário o elemento possui como pai o nó atual
                        lista.insert(cont,x)
                cont += 1

        print("-",end = '')
        for x in lista:
            print(x.nome,end= "-")
        print("")
    #==============================================       FIM DO WHILE            ========================================================
print("oi")
HillClimbing(nodeS)