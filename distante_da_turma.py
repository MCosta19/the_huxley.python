notas= []
maior= 0
distan= []
nome_m= 'x'

for i in range(5):
    nota= float(input())
    notas.append(nota)
    nome= input()

    if nota > maior:
        maior = nota
        nome_m = nome

media= sum(notas)/len(notas)

for j in notas:
    dist= media-j
    distan.append(dist)

for k in notas:
    print(f'{k:.2f}', end=' ')

print('')
print(f'{media:.2f}')

for l in distan:
    print(f'{l:.2f}', end=' ')

print('')
print(nome_m.capitalize())
print(notas.index(max(notas)))