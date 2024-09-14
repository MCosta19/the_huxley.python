#Ambrosio romantico

n,e= input().split()

n= int(n)
e= int(e)

ideia= [int(x) for x in input().split()]
    
for i in ideia+[1]:
    
    if i>e:
        ideia.remove(i)
        
for j in range(len(ideia)):
    
    if ideia>[]:
        mini= min(ideia)
        maxm= max(ideia)
        
        if maxm+mini>e or maxm+mini<e:
            ideia.remove(min(ideia))
            ideia.remove(max(ideia))

        else:
            break

    else:
        break

    
if maxm+mini==e:
    print('SIM')

elif ideia== []:
    print('NAO')
#print(ideia)