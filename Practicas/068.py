numeros = [0, 1, 0, 3, 12, 0, 5]

for num in numeros:
    if num==0:
        numeros.remove(num)
        numeros.append(0)

print(numeros)