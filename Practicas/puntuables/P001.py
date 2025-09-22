palabra = input("Ingresa una palabra:").lower()
contador = 0
for letra in palabra:
    if letra in 'aeiou':
        contador += 1

print(contador)