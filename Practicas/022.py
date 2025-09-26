operacion = int(input("Ingresa una operacion: 1= * ,2= - , 3= + ,4 = / "))
numero1 = int(input("Ingresa una numero : "))
numero2 = int(input("Ingresa una numero : "))

match operacion:
    case 4:
        if numero1 > numero2:
            print(f"El resultado de {numero1} / {numero2} ={numero1/numero2}")
        elif numero1 < numero2:
            print(f"El resultado de {numero2} / {numero1} ={numero2 / numero1}")

    case 1:
        print(f"El resultado de {numero2} * {numero1} ={numero2 * numero1}")
    case 2:
        print(f"El resultado de {numero2} - {numero1} ={numero2 - numero1}")
    case 3:
        print(f"El resultado de {numero2} + {numero1} ={numero2 + numero1}")
