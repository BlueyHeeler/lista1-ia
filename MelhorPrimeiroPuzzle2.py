from ClasseTabuleiro import Tabuleiro
import copy
tabuleiro = Tabuleiro([[1,2,3],[8,0,4],[7,6,5]])
def puzzle(tabuleiro):
    cont2 = 0                                               #analiza tabuleiro
    cont3 = 0        
    cont4 = 0                                               #linha do 0
    listaDeTabuleiros = []                                  #lista de tabuleiros
    listaDeTabuleiros2 = []                                 #lista de tabuleiros já visitados
    listaDeTabuleiros3 = []
    for x in range(5000):
        for x in tabuleiro.tabuleiro:
            print(x)
        print(tabuleiro.get_valor())
        tabuleiroW = Tabuleiro(copy.deepcopy(tabuleiro.tabuleiro))
        tabuleiroS = Tabuleiro(copy.deepcopy(tabuleiro.tabuleiro))
        tabuleiroA = Tabuleiro(copy.deepcopy(tabuleiro.tabuleiro))
        tabuleiroD = Tabuleiro(copy.deepcopy(tabuleiro.tabuleiro))
       
        if tabuleiro.valor == 8:                            #Verifica o valor da posição
            break
        cont3 = 0
        for x in tabuleiro.tabuleiro:                       #identifica a posição do 0                            
            if 0 in x:
                cont4 = cont3                               #linha
                index = x.index(0)                          #coluna
            cont3 += 1
        lista = []
        #W      
        if cont4 - 1 < 0:
            pass
        else:
            if tabuleiroW.tabuleiro in listaDeTabuleiros2:
                pass
            else:
                tabuleiroW.previous = tabuleiro
                lista = [tabuleiroW.tabuleiro[cont4].pop(index)]       #remove o 0 e o adiciona a uma lista
                lista += [tabuleiroW.tabuleiro[cont4-1].pop(index)]    #remove o número acima do 0 e o adiciona a uma lista
                tabuleiroW.tabuleiro[cont4-1].insert(index,lista[0])   #insere o 0    
                tabuleiroW.tabuleiro[cont4].insert(index,lista[1])     #insere o número
                tabuleiroW = Tabuleiro(tabuleiroW.tabuleiro)
                if tabuleiroW.tabuleiro in listaDeTabuleiros3 :
                    pass
                else:
                    listaDeTabuleiros.append(tabuleiroW)                   #insere na lista
                    listaDeTabuleiros3.append(tabuleiroW.tabuleiro)
        lista = []
        #S    
        if cont4 + 1 > 2:
            pass
       
        else:
            if tabuleiroS.tabuleiro in listaDeTabuleiros2:
                pass
            else:
                tabuleiroS.previous = tabuleiro
                lista = [tabuleiroS.tabuleiro[cont4].pop(index)]       #remove o 0 e o adiciona a uma lista
                lista += [tabuleiroS.tabuleiro[cont4+1].pop(index)]    #remove o número acima do 0 e o adiciona a uma lista
                tabuleiroS.tabuleiro[cont4+1].insert(index,lista[0])   #insere o 0    
                tabuleiroS.tabuleiro[cont4].insert(index,lista[1])     #insere o número
                tabuleiroS = Tabuleiro(tabuleiroS.tabuleiro)
                if tabuleiroS.tabuleiro in listaDeTabuleiros3 :
                    pass
                else:
                    listaDeTabuleiros.append(tabuleiroS)                   #insere na lista
                    listaDeTabuleiros3.append(tabuleiroS.tabuleiro)
        lista = []
        #D  
        if index + 1 > 2:
            pass
       
        else:
            if tabuleiroD.tabuleiro in listaDeTabuleiros2:
                pass
            else:
                tabuleiroD.previous = tabuleiro
                lista = [tabuleiroD.tabuleiro[cont4].pop(index)]       #remove o 0 e o adiciona a uma lista
                lista += [tabuleiroD.tabuleiro[cont4].pop(index)]      #remove o número acima do 0 e o adiciona a uma lista
                tabuleiroD.tabuleiro[cont4].insert(index,lista[0])     #insere o 0    
                tabuleiroD.tabuleiro[cont4].insert(index,lista[1])     #insere o número
                tabuleiroD = Tabuleiro(tabuleiroD.tabuleiro)
                if tabuleiroD.tabuleiro in listaDeTabuleiros3 :
                    pass
                else:
                    listaDeTabuleiros.append(tabuleiroD)                   #insere na lista
                    listaDeTabuleiros3.append(tabuleiroD.tabuleiro)
        lista = []
        #A    
        if index - 1 < 0:
            pass
       
        else:
            if tabuleiroA.tabuleiro in listaDeTabuleiros2:
                pass
            else:
                tabuleiroA.previous = tabuleiro
                lista = [tabuleiroA.tabuleiro[cont4].pop(index)]       #remove o 0 e o adiciona a uma lista
                lista += [tabuleiroA.tabuleiro[cont4].pop(index-1)]    #remove o número acima do 0 e o adiciona a uma lista
                tabuleiroA.tabuleiro[cont4].insert(index-1,lista[0])   #insere o 0    
                tabuleiroA.tabuleiro[cont4].insert(index,lista[1])     #insere o número
                tabuleiroA = Tabuleiro(tabuleiroA.tabuleiro)
                if tabuleiroA.tabuleiro in listaDeTabuleiros3 :
                    pass
                else:
                    listaDeTabuleiros.append(tabuleiroA)                   #insere na lista
                    listaDeTabuleiros3.append(tabuleiroA.tabuleiro)

        listaDeTabuleiros2.append(tabuleiro)
        sorted_tabuleiros = sorted(listaDeTabuleiros, key=lambda tabuleiro: tabuleiro.valor, reverse = True)
        for x in listaDeTabuleiros2:
            if x in sorted_tabuleiros:
                #print("oi")
                sorted_tabuleiros.remove(x)
        tabuleiro = sorted_tabuleiros[0]
        #for x in sorted_tabuleiros:
            #print(x.tabuleiro)
        print("=========================")
        #for x in listaDeTabuleiros2:
            #print(x.tabuleiro)
        print("=========================")
        #for x in listaDeTabuleiros3:
           # print(x)
        tabuleiroTeste = tabuleiro
       
puzzle(tabuleiro)