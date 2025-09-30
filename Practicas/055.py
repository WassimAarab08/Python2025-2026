lista = []
numeroDado=22
resultado = True
for i  in range(2,numeroDado-1):
    for num in range(2, i - 1):
        if i % num == 0:
            resultado = False

    if resultado:
        lista.append(i)
    else:
        resultado = True


print(lista)