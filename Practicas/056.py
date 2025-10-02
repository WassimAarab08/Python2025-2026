

lista = ["moda", "moda", "carlos", "azucar", "lopez", "lopez", "moda"]
palabrasSinRepetir=[]
repeticiones = []
ordenModa=[]

for palabra in lista:
    if palabra not in palabrasSinRepetir:
        palabrasSinRepetir.append(palabra)
        repeticiones.append(0)


for i in range(len(palabrasSinRepetir)):
     for palabra in lista:
         if palabra == palabrasSinRepetir[i] :
             repeticiones[i]= repeticiones[i]+1

moda1=palabrasSinRepetir[1]
indices = 1
for i in range(2):
    numeroRepeticiones = 1
    for i in range(len(palabrasSinRepetir)):
        if repeticiones[i]>=numeroRepeticiones:
          moda1=palabrasSinRepetir[i]
          numeroRepeticiones=repeticiones[i]

          indices=i

    ordenModa.append(moda1)
    ordenModa.append(numeroRepeticiones)
    palabrasSinRepetir.pop(indices)
    repeticiones.pop(indices)

print(lista)
print(palabrasSinRepetir)
print(repeticiones)
print(f"La primera moda es {ordenModa[0]} con {ordenModa[1]} repeticiones ")
print(f"La segunda moda es {ordenModa[2]} con {ordenModa[3]} repeticiones ")




