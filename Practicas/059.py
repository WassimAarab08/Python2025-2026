numeroAcambiar=int(input("Que numero quieres cambiar ? => "))
numeroDado=int(input("Por que numero lo quieres cambiar ? => "))

numeros=[1,2,3,4,5,6,7,8,9,10,3,4,2,4,2,321,3,13,23,3,23]
print(numeros)
print("=======================================================")
for i in range(len(numeros)):

    if numeros[i]==numeroAcambiar:
        numeros[i]=numeroDado

print(numeros)