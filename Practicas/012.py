flag = True
suma = 0
while flag :
    numeroSolicitado = int(input("Introduce un numero: "))
    if numeroSolicitado == 0:
        flag = False
    suma += numeroSolicitado


print("La suma es " , suma)
