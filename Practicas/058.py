numerosRepetidos = [5, 2, 7, 5, 3, 2, 8, 5, 7, 1, 3, 2,0]
numeros=[]
contador=0
for n in numerosRepetidos:
    if n not in numeros:
        numeros.append(n)
        for num in numerosRepetidos:
            if num == n:
              contador+=1
        numeros.append(contador)
        contador=0


for i in range(0,len(numeros),+2):
  print(f"{numeros[i]}:{numeros[i+1]}")