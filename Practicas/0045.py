
compañeros =["Misael","Carlos","Hugo","Alvaro","Alex"]
ascendente = []


while compañeros:
    minimo = compañeros[0]
    for palabra in compañeros:
        if palabra < minimo:
            minimo = palabra
    ascendente.append(minimo)
    compañeros.remove(minimo)

print("Ascendente:", ascendente)



