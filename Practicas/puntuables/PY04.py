import random


numeroRandom=random.randint(1,200)
intentos =6

while 0<intentos :
    num=int(input("Introduce el numero =>"))
    if num==numeroRandom:
        print("Has adividando el numero")
        flag=False
    else:
        print("incorrecto")
        intentos=intentos-1

