for i in range(15):
    n= int(input())

    par= []
    impar= []

    if len(par)==5:
        for j in par:
            print('par[',par.index(j),'] = ',j, sep='')
        par.clear()

    if n%2 == 0:
        par+= [n]

    if len(impar)==5:
        for k in impar:
            print('par[',par.index(k),'] = ',k, sep='')

    if n%2 != 0:
        impar+= [n]
