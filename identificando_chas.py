#Identificando chás

t= int(input())

lista=[]

a, b, c, d, e= input().split()

a= int(a)
b= int(b)
c= int(c)
d= int(d)
e= int(e)

if (a==t):
  lista.append(a)

if (b==t):
  lista.append(b)

if (c==t):
  lista.append(c)

if (d==t):
  lista.append(d)

if (e==t):
  lista.append(e)

if (lista==0):
  print(0)

else:
  print(len(lista))