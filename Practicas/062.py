numerosRepetidos = [5, 2, 7, 5, 3, 2, 8, 5, 7, 1, 3, 2,0]
numeroDado=5
numerosMenores=[]
numerosMayores=[]


for n in numerosRepetidos:
    if n<=numeroDado:
        numerosMayores.append(n)
    else:
        numerosMenores.append(n)


print("Lista menor => ",numerosMenores)
print("Lista mayor => ",numerosMayores)