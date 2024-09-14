#Exibindo notas e posição

n= int(input())

notas= []

if n<=0:
  print('Numero de notas invalido.')

else:
  for i in range(n):
    nota= float(input())

    notas.append(nota)


  for j in notas:

    print('Nota ', (notas.index(j))+1,': ', j, sep='')

  media= (sum(notas)/len(notas))
  print(f'Media: {media:.2f}')