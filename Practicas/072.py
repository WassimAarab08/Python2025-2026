

numeroDado = int(input("Dame un numero de menos de tres digitos => "))
while 1000 < numeroDado < 0:
    numeroDado = int(input("Dame un numero de menos de tres digitos =>"))

bandera = True
divisor=2
resultado = 0
for num in range(2,numeroDado-1):
    if numeroDado % num == 0:
        bandera = True


while bandera:
    if numeroDado == 1:
        bandera=False
    if numeroDado%divisor ==0:
        numeroDado=numeroDado/divisor
        print(divisor, end="x")
    else:
        divisor=divisor+1

print("1")