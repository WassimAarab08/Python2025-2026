numeros1=[1,2,3,4,5,6,7,3,5,333,55,22,33,55,66,7,33]
numerosInvertidos = []
i=len(numeros1)-1

while i >= 0:
     print(i)
     numerosInvertidos.append(numeros1[i])
     i-=1

print(numeros1)
print(numerosInvertidos)