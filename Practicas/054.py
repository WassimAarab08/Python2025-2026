numero= 36

resultado = True

for num in range(2,numero-1):
    if numero % num == 0:
        resultado = False

if resultado:
    print("Es primo")
else:
    print("No es primo")