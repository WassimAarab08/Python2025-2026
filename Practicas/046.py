list=["w","r","u","a","i","g"]
contador=0
for letra in list:
    if letra in "aueio":
        contador+=1

print(f"Hay {contador} vocales")