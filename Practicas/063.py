numerosRepetidos = [5, 2, 7, 5, 3, 2, 8, 5, 7, 1, 3, 2,0]
impares=0
pares=0


for n in numerosRepetidos:
    if n%2==0:
        pares +=1
    else:
        impares+=1


print("Impares =>", impares)
print("Pares =>",pares)