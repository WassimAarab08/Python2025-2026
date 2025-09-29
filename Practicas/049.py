listaDuplicada=["wassim","wassim","carlos","misael","carlos"]
listaSinDup=[]

for item in listaDuplicada:
   if item not in listaSinDup:
       listaSinDup.append(item)


print(listaSinDup)