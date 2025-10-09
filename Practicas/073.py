numeroDado="369"

for i in range(len(numeroDado)):

    if numeroDado[i]== numeroDado[0]:
        print(numeroDado[i],"centenas")
    elif numeroDado[i]== numeroDado[1]:
        print(numeroDado[i],"decenas")
    else:
        print(numeroDado[i], "unidades")

