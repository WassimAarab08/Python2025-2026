numero = int(input("Escribe un numero: "))

for i in range(1,numero+1):
   if numero % i ==0 :
       print(f"{i}", end=" ")
    