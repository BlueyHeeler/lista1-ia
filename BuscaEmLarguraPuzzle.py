import copy
tabuleiro = [[1,2,3],
             [4,0,8],
             [7,6,5]]

def puzzle(tabuleiro):

    lista = []                                                                      #guarda tabuleiros
    lista2 = []                                                                     #guarda tabuleiros já vistiados
    caminho = {}                                                                    #caminho
    MainTabuleiro = tabuleiro
    lista2.append(tabuleiro)
    iteracoes = 0

    caminho[tuple(tuple(x) for x in MainTabuleiro)] = None
    for x in range(10000):
        print(MainTabuleiro)
        tabuleiroW = copy.deepcopy(MainTabuleiro)                                   #replicas do tabuleiro original
        tabuleiroS = copy.deepcopy(MainTabuleiro)
        tabuleiroA = copy.deepcopy(MainTabuleiro)
        tabuleiroD = copy.deepcopy(MainTabuleiro)

        valor = analizaTabuleiro(MainTabuleiro)

        if valor == 8:                                                              #caso em que o puzzle foi resolvido
            break

        cont = 0                                                                    #contador
        for x in MainTabuleiro:                                                     #identifica a posição do 0                             
            if 0 in x:
                linha = cont                                                        
                coluna = x.index(0)                                                 
            cont += 1

        if linha - 1 < 0:
            pass
        else:
            temp = W(tabuleiroW,linha,coluna)
            if temp in lista2:
                pass
            else:
                lista.append(temp)
                caminho[tuple(tuple(x) for x in temp)] = MainTabuleiro

        if linha + 1 > 2:
            pass
        else:
            temp = S(tabuleiroS,linha,coluna)
            if temp in lista2:
                pass
            else:
                lista.append(temp)
                caminho[tuple(tuple(x) for x in temp)] = MainTabuleiro
            
        if coluna + 1 > 2:
            pass
        else:
            temp = D(tabuleiroD,linha,coluna)
            if temp in lista2:
                pass
            else:
                lista.append(temp)
                caminho[tuple(tuple(x) for x in temp)] = MainTabuleiro

        if coluna - 1 < 0:
            pass
        else:
            temp = A(tabuleiroA,linha,coluna)
            if temp in lista2:
                pass
            else:
                lista.append(temp)
                caminho[tuple(tuple(x) for x in temp)] = MainTabuleiro

        for x in lista2:
            while x in lista:
                lista.remove(x)

        MainTabuleiro = copy.deepcopy(lista[0])
        lista2.append(copy.deepcopy(lista[0]))
        lista.pop(0)
        iteracoes += 1

    print("ACHOU")
    print(iteracoes)    
    x = MainTabuleiro
    while x != None:
        print(x)
        x = caminho[tuple( tuple(y) for y in x)]

        
        

def W(tabuleiro,linha,coluna):
    tabuleiroW = tabuleiro
    cont4 = linha
    index = coluna

    lista = [tabuleiroW[cont4].pop(index)]                                  #remove o 0 e o adiciona a uma lista
    lista += [tabuleiroW[cont4-1].pop(index)]                               #remove o número acima do 0 e o adiciona a uma lista
    tabuleiroW[cont4-1].insert(index,lista[0])                              #insere o 0     
    tabuleiroW[cont4].insert(index,lista[1])                                #insere o número

    return tabuleiroW

def S(tabuleiro,linha,coluna):
    tabuleiroS = tabuleiro
    cont4 = linha
    index = coluna

    lista = [tabuleiroS[cont4].pop(index)]                                  #remove o 0 e o adiciona a uma lista
    lista += [tabuleiroS[cont4+1].pop(index)]                               #remove o número abaixo do 0 e o adiciona a uma lista
    tabuleiroS[cont4+1].insert(index,lista[0])                              #insere o 0     
    tabuleiroS[cont4].insert(index,lista[1])                                #insere o número
    

    return tabuleiroS

def A(tabuleiro,linha,coluna):
    tabuleiroA = tabuleiro
    cont4 = linha
    index = coluna

    lista = [tabuleiroA[cont4].pop(index)]                                  #remove o 0 e o adiciona a uma lista
    lista += [tabuleiroA[cont4].pop(index-1)]                               #remove o número a esquerda do 0 e o adiciona a uma lista
    tabuleiroA[cont4].insert(index-1,lista[0])                              #insere o 0     
    tabuleiroA[cont4].insert(index,lista[1])                                #insere o número

    return tabuleiroA

def D(tabuleiro,linha,coluna):
    tabuleiroD = tabuleiro
    cont4 = linha
    index = coluna

    lista = [tabuleiroD[cont4].pop(index)]                                  #remove o 0 e o adiciona a uma lista
    lista += [tabuleiroD[cont4].pop(index)]                                 #remove o número a direita do 0 e o adiciona a uma lista
    tabuleiroD[cont4].insert(index,lista[0])                                #insere o 0     
    tabuleiroD[cont4].insert(index,lista[1])                                #insere o número

    return tabuleiroD

def analizaTabuleiro(tabuleiro):                                                    #Verifica o valor da posição
    cont= 1
    cont2 = 0
    for x in tabuleiro:                                                             #analiza a posição dos números caso o número esteja na casa correta é somado ao cont2 +1
            for y in x:
                if y == cont:
                    cont2 +=1
                cont+=1
    return cont2

teste = puzzle(tabuleiro)