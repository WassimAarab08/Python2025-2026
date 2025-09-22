tablaDel = int (input("Ingresa un numero para imprimir su tabla de multiplicacion: "))
numero =  int (input("Ingresa el fin de la tabla: "))
for i in range (numero):
    print(f" {tablaDel}x{numero}=",tablaDel * i)