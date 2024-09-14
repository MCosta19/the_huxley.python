#Quantos numeros

n= int(input())

lista= []

cont= 0

maior= 0

menor= 0

for i in  range(n):

  num= int(input())

  lista.append(num)

  cont+=num

media= cont/n

print(f'{media:.2f}')

media_maior= media*1.10

media_menor= (-media)*-1.10

for j in lista:

  if j > media_maior:

    maior+=1

  elif j < media_menor:

    menor+=1

print(maior)

print(menor)