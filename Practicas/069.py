numeros = [10, 30, 15, 2, 45, 60, 5, 100, 35]
numerosElminados = numeros
grandes=[]

for n in range ( 3):
    maximo = numerosElminados[0]
    for num in numerosElminados:
        if maximo<num:
            maximo = num
    grandes.append(maximo)
    numerosElminados.remove(maximo)

print(grandes)

