#garçom

n= int(input())
quebrados= []

for i in range(n):
  latas, copos= input().split()

  latas= int(latas)
  copos= int(copos)

  if latas>copos:
    quebrados.append(copos)

print(sum(quebrados))