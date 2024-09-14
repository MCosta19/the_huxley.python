#intercalar um array

n= int(input())
lista_1= []

lista_2= []

lista_3= []

lista_4= []

for i in range(n):
  num= int(input())

  lista_1.append(num)

for i in range(n):
  num_2= int(input())

  lista_2.append(num_2)

for i in range(n):
  lista_3 = [lista_1[0], lista_2[0]]
  lista_4 += lista_3

  del lista_1[0]

  del lista_2[0]

for i in lista_4:
  print(i)