numero = float(input("Introduce  la cantidad de metros: "))
unidad = input("Introduce la unidad km, m, cm => ")

match unidad:
    case "km":
        print(f"{numero} km = {numero * 1000} m")
    case "m":
        print(f"{numero} m = {numero} m")
    case "cm":
        print(f"{numero} cm = {numero / 100} m")
    case _:
        print("Opcion no valida")