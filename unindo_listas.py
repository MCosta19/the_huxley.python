#Unindo listas

n= int(input())
lista_1= []

if n <=0:

  print("Erro - A lista deve ter pelo menos 1 elemento.")

else:

  for i in range(n):

    num= int(input())

    lista_1.append(num)

  n2= int(input())
  lista_2= []

  if n2<=0:

    print("Erro - A lista deve ter pelo menos 1 elemento.")

  else:

    for j in range(n2):

      num2= int(input())

      lista_2.append(num2)

    lista_3= lista_1 + lista_2

    for k in lista_3:

      print(k, end=' ')
