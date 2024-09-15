par= []
impar= []

for i in range(15):
    n= int(input())

    if len(par)==5:
        for j in par:
            print('par[',par.index(j),'] = ',j, sep='')
        par.clear()

    if n%2 == 0:
        par+= [n]

    if len(impar)==5:
        for k in impar:
            print('impar[',impar.index(k),'] = ',k, sep='')
        impar.clear()

    if n%2 != 0:
        impar+= [n]

if len(impar) > 0:
    for l in impar:
        print('impar[',impar.index(l),'] = ',l, sep='')

if len(par) > 0:
    for m in par:
        print('par[',par.index(m),'] = ',m, sep='')