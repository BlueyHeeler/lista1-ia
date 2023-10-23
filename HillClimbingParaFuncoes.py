#HillClimbing para encontrar mínimos de uma função quadrática
#f(x) = ax**2+bx+c

a = float(input())
b = float(input())
c = float(input())
x = float(input())                               #chute inicial
y = float(x-0.1)
z = float(x+0.1)
lista = []
def funcao(a,b,c,x):
    funcao = float(a*(x**2)+ b*x +c)
    return funcao
funcao1 = funcao(a,b,c,y)
funcao2 = funcao(a,b,c,z)
lista.append(funcao1)
lista.append(funcao2)
if a > 0:
    if lista[0] < lista[1]:
        while lista[0] < lista[1]:
            y = y - 0.1
            z = z - 0.1
            funcao1 = funcao(a,b,c,y)
            funcao2 = funcao(a,b,c,z)
            lista[0]=(funcao1)
            lista[1]=(funcao2)
        media = (y + z)/2
        print(f"o mínimo local está aproximadamente em :{media}")
    else:
        while lista[0] > lista[1]:
            y = y + 0.1
            z = z + 0.1
            funcao1 = funcao(a,b,c,y)
            funcao2 = funcao(a,b,c,z)
            lista[0]=(funcao1)
            lista[1]=(funcao2)
        media = (y + z)/2
        print(f"o mínimo local está aproximadamente em :{media}")
else:
    print("só serve para encontrar mínimos")