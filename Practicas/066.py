numerosRepetidos = [5, 2, 7, 5, 3, 2, 8, 5, 7, 1, 3, 2,0]
sumatorio= 0

for num in numerosRepetidos:
    if num%2!=0:
        sumatorio= sumatorio+ num


print("Resultado =>",sumatorio)