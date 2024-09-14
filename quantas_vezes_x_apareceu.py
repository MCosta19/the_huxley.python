#quantas vezes x apareceu?

lista= []

for i in range(1,11):
  num= int(input())
  lista.append(num)

x= int(input())

cont= 0

for i in lista:
  if i==x:
    cont+=1

print(cont)