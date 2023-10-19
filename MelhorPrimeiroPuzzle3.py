from ClasseTabuleiro import Tabuleiro
import copy
tabuleiro = [[1,2,3],
             [4,8,0],
             [7,6,5]]

def puzzle(tabuleiro):

    lista = []                                                                      #guarda tabuleiros
    lista2 = []                                                                     #guarda tabuleiros já vistiados
    temp = tabuleiro
    tabuleiroOriginal = Tabuleiro(tabuleiro,analizaTabuleiro(tabuleiro))
    tabuleiroOriginal.previous = None

    for x in range(6):
        print("-----------")
        print(temp)
        print("-----------")
        tabuleiroW = copy.deepcopy(temp)                                            #replicas do tabuleiro original
        tabuleiroS = copy.deepcopy(temp)
        tabuleiroA = copy.deepcopy(temp)
        tabuleiroD = copy.deepcopy(temp)

        valor = analizaTabuleiro(temp)
        print(valor)
        if valor == 8:                                                              #caso em que o puzzle foi resolvido
            break

        cont = 0                                                                    #contador
        for x in temp:                                                              #identifica a posição do 0                             
            if 0 in x:
                linha = cont                                                        
                coluna = x.index(0)                                                 
            cont += 1

        if linha - 1 < 0:
            pass
        else:
            if W(tabuleiroW,linha,coluna) in lista:
                lista.append(W(tabuleiroW,linha,coluna))
            else:
                lista.append(W(tabuleiroW,linha,coluna))
                tabuleiroW2 = Tabuleiro(W(tabuleiroW,linha,coluna),analizaTabuleiro(tabuleiroW))
                tabuleiroW2.previous = tabuleiroOriginal
                lista2.append(tabuleiroW2)


        if linha + 1 > 2:
            pass
        else:
            if S(tabuleiroS,linha,coluna) in lista:
                lista.append(S(tabuleiroS,linha,coluna))
            else:
                lista.append(S(tabuleiroS,linha,coluna))
                tabuleiroS2 = Tabuleiro(S(tabuleiroS,linha,coluna),analizaTabuleiro(tabuleiroS))
                tabuleiroS2.previous = tabuleiroOriginal
                lista2.append(tabuleiroS2)
            

        if coluna + 1 > 2:
            pass
        else:
            if D(tabuleiroD,linha,coluna) in lista:
                lista.append(D(tabuleiroD,linha,coluna))
            else:
                lista.append(D(tabuleiroD,linha,coluna))
                tabuleiroD2 = Tabuleiro(D(tabuleiroD,linha,coluna),analizaTabuleiro(tabuleiroD))
                tabuleiroD2.previous = tabuleiroOriginal
                lista2.append(tabuleiroD2)

        if coluna - 1 < 0:
            pass
        else:
            if A(tabuleiroA,linha,coluna) in lista:
                lista.append(A(tabuleiroA,linha,coluna))
            else:
                lista.append(A(tabuleiroA,linha,coluna))
                tabuleiroA2 = Tabuleiro(A(tabuleiroA,linha,coluna),analizaTabuleiro(tabuleiroA))
                tabuleiroA2.previous = tabuleiroOriginal
                lista2.append(tabuleiroA2)

        #print("============")
        sorted_tabuleiros = sorted(lista2, key=lambda tabuleiro: tabuleiro.valor, reverse = True)
        proximo = copy.deepcopy(sorted_tabuleiros[0])
        for x in sorted_tabuleiros:
            print(x.tabuleiro)
        sorted_tabuleiros.pop(0)
        print("=====================")
        for x in sorted_tabuleiros:
            print(x.tabuleiro)
        print("======================")
        for x in lista:
            print(x)
        tabuleiroOriginal = proximo
        temp = copy.deepcopy(proximo.tabuleiro)
        #print("===========")
        #for x in lista:
            #print(x)
        #print("============")
    #print("-----------------------------------------")
    #print(tabuleiroOriginal.tabuleiro)
    #z = tabuleiroOriginal.tabuleiro
    #while z != [[4,3,6],
             #[1,7,2],
             #[5,8,0]]:
        #tabuleiroOriginal = tabuleiroOriginal.previous
        #z = tabuleiroOriginal.tabuleiro
        #print(z)
    #for x in sorted_tabuleiros:
        #print(x.tabuleiro)
    


        

def analizaTabuleiro(tabuleiro):                                                    #Verifica o valor da posição
    cont= 1
    cont2 = 0
    for x in tabuleiro:                                                             #analiza a posição dos números caso o número esteja na casa correta é somado ao cont2 +1
            for y in x:
                if y == cont:
                    cont2 +=1
                cont+=1
    return cont2

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

aaa = puzzle(tabuleiro)