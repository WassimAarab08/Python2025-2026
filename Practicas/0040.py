original = [5, 2, 9, 1, 5, 6]


ascendente = []
temp = original.copy()
while temp:
    minimo = temp[0]
    for num in temp:
        if num < minimo:
            minimo = num
    ascendente.append(minimo)
descendente = ascendente[::-1]

print("Original   :", original)
print("Ascendente :", ascendente)
print("Descendente:", descendente)
