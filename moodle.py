#moodle 1, 2, 3, 4

# mercado= ["cuscuz", "arroz", "macarrão"]

lista= ['A', 'B', 12]

del lista[2]
# del lista[0]
lista.remove('A')

print(lista)

#moodle 5

idades= []

while True:
  idade= int(input())

  if idade<0:
    break

  else:
    idades.append(idade)
    idades.sort()

for i in range(len(idades)):
  print(idades[i])

media= (sum(idades))/len(idades)

print(idades[0])
print(idades[-1])
print(media)

#moodle 6

n= int(input())

premiados= []

for i in range(n):
  nome= input()
  nota= int(input())

  if nota>=80:
    premiados.append(nome)
    premiados.append(nota)

print(premiados)