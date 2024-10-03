cine= 0
bol= 0

for i in range(7):
    escolha= input().upper()
    
    if escolha == 'CINEMA':
        cine += 1

    elif escolha == 'BOLICHE':
        bol += 1

if cine > bol:
    print('CINEMA')

elif bol > cine:
    print('BOLICHE')
