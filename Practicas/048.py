frase=input("escribe una palabra =>")
palabra = frase.split(" ")
contador= 0

for n in palabra:
    contador+=1

print(f"Hay {contador} palabras")