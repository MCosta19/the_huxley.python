altura= []

for i in range(4):
    n= float(input())
    altura += [n]

altura.sort()

print(f'{altura[0]:.2f}')
print(f'{altura[2]:.2f}')
print(f'{altura[3]:.2f}')
print(f'{altura[1]:.2f}')