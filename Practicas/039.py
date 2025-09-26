numeros = [1, 2, 2, 3, 4, 4, 4, 5]
numerosMultiplicados =[]
multiplicador = int(input("Ingresa un numero por el que multiplicar todos los elementos de la lista: "))

for i in numeros:
    numerosMultiplicados.append(multiplicador*i)

print(numerosMultiplicados)