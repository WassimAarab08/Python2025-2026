
import random
max= int(input("Escribe el limite superior del random => "))
min= int(input("Escribe el limite inferior del random => "))
intentos = int(input("Escribe la cantidad de elementos random a generar => "))

for i in range(intentos):
    num = random.randint(min, max)
    print(num)