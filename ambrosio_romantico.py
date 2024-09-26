n , e= input().split()
n= int(n)
e= int(e)
lista= (input().split())
saida= 'NAO'

for i in range(n):
    p = int(lista[i])
    soma = 0

    for j in lista:
        q = int(j)


        if q != p:
            soma = p + q

        if soma == e:
            saida = 'SIM'

print(saida)