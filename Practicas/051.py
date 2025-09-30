numeros=[1,2,3,4,5,6,7,3,5,333,55,22,33,55,66,7,33]
numerosNoOredenados=[]
numeroOrdenados = []
numeroDado=int(input("Escribe un numero =>"))


for n in numeros :
    if n > numeroDado:
        numerosNoOredenados.append(n)

while numerosNoOredenados:
    axuliar = numerosNoOredenados[0]
    for nu in numerosNoOredenados:
      if axuliar > nu:
        axuliar = nu
    numeroOrdenados.append(axuliar)
    numerosNoOredenados.remove(axuliar)


print(numeroOrdenados)
print("El numero max es => ", numeroOrdenados[len(numeroOrdenados)-1])



