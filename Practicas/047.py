numeros=[1,2,3,44,105,55,6,44,88]
numMax=numeros[1]
for n in numeros:
   if numMax < n:
       numMax=n

print(f"El numero maximo es {numMax}")