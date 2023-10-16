tabuleiro = [[1,2,3],
             [4,5,6],
             [7,0,8]]
def puzzle(tabuleiro):
    cont = 1                                                #cont e cont2 são utilizados para verificar a posição dos itens
    cont2= 0
    cont3 = 0        
    cont4 = 0                                               #linha do 0
    while True:
                                                            #Verifica o valor da posição
        for x in tabuleiro:                                 #analiza a posição dos números caso o número esteja na casa correta é somado ao cont2 +1
            print(x)
            for y in x:
                if y == cont:
                    cont2 +=1
                cont+=1
        print(cont2)
        if cont2 == 8:
            break
        cont = 1                                            #reset do cont
        cont2 = 0                                           #reset do cont
        cont3 = 0
        for x in tabuleiro:                                 #identifica a posição do 0                             
            if 0 in x:
                cont4 = cont3                               #linha
                index = x.index(0)                          #coluna
            cont3 += 1
        x = input()
        if x == "w":
            if cont4 - 1 < 0:
                pass
            else:
                lista = [tabuleiro[cont4].pop(index)]       #remove o 0 e o adiciona a uma lista
                lista += [tabuleiro[cont4-1].pop(index)]    #remove o número acima do 0 e o adiciona a uma lista
                tabuleiro[cont4-1].insert(index,lista[0])   #insere o 0     
                tabuleiro[cont4].insert(index,lista[1])     #insere o número
        elif x == "s":
            if cont4 + 1 > 2:
                pass
            else:
                lista = [tabuleiro[cont4].pop(index)]       #remove o 0 e o adiciona a uma lista
                lista += [tabuleiro[cont4+1].pop(index)]    #remove o número abaixo do 0 e o adiciona a uma lista
                tabuleiro[cont4+1].insert(index,lista[0])   #insere o 0     
                tabuleiro[cont4].insert(index,lista[1])     #insere o número
        elif x == "d":
            if index + 1 > 2:
                pass
            else:
                lista = [tabuleiro[cont4].pop(index)]       #remove o 0 e o adiciona a uma lista
                lista += [tabuleiro[cont4].pop(index)]      #remove o número a direita do 0 e o adiciona a uma lista
                tabuleiro[cont4].insert(index,lista[0])     #insere o 0     
                tabuleiro[cont4].insert(index,lista[1])     #insere o número
        elif x == "a":
            if index - 1 < 0:
                pass
            else:
                lista = [tabuleiro[cont4].pop(index)]       #remove o 0 e o adiciona a uma lista
                lista += [tabuleiro[cont4].pop(index-1)]    #remove o número a esquerda do 0 e o adiciona a uma lista
                tabuleiro[cont4].insert(index-1,lista[0])   #insere o 0     
                tabuleiro[cont4].insert(index,lista[1])     #insere o número
            
puzzle(tabuleiro)
