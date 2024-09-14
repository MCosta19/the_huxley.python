#Menor valor e posição

n= int(input())

lista= [int (x) for x in input().split() ]

menor= min(lista)

print('Menor valor:', menor)

print(f'Posicao: {lista.index(min(lista))}')