

ListaMixta = [["Perro","Pajaro","Leon",["Manzana","Platano","Pera"]]]
i=0
for array in ListaMixta:
   for a in array:
       if a != array[-1]:
           print(a, end=" ")
       else:
           print()
           for i in a:
               print(i, end=" ")