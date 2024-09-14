#A corrida da escola

num_com,num_vol= input().split()

tempo= []

soma_tempo= []

num_com= int(num_com)
num_vol= int(num_vol)

for i in range(num_com):
    
    tempo= [int(x) for x in input().split() ]

    soma_tempo.append(sum(tempo))

print(soma_tempo.index(min(soma_tempo)) + 1)