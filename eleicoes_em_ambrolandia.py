alibaba= []
alcapone= []
branco= []
nulo= []
total= []

while True:
    voto= int(input())

    if voto == -1:
        break

    if voto == 83:
        alibaba += [1]
        total += [1]

    elif voto == 93:
        alcapone += [1]
        total += [1]

    elif voto == 0:
        branco += [1]
        total += [1]

    elif (voto != 0, 83, 93):
        nulo += [1]

perc_ali= (len(alibaba)/len(total))*100
perc_alc= (len(alcapone)/len(total))*100

print(len(alibaba))
print(len(alcapone))
print(len(branco))
print(len(nulo))

if len(alibaba) > len(alcapone):
    print(83)

else:
    print(93)

print(f'{perc_ali:.2f}')
print(f'{perc_alc:.2f}')