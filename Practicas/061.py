lista = ["moda", "moda","carlos", "azucar", "lopez", "moda"]

for i in range(len(lista)-1,-1,-1)  :
    palabra=lista[i]

    if len(palabra) <= 4:
        lista.pop(i)


print(lista)