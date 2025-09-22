x = int( input("Dime el eje x de cuadrado: "))
y=int( input("Dime el eje y de cuadrado: "))
motivo = input("Dime el motivo de cuadrado: ")
for j in range(x):
    for i in range(y):
        print(motivo, end=" ")
    print()