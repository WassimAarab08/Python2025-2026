diaSemana =input("Dia de semana para saber si es laborable: ").lower()

match diaSemana:
    case "sabado"  :
        print("No es laborable")
    case "domingo":
        print("No es laborable")
    case "lunes"| "martes" | "miercoles" | "jueves" | "viernes":
        print("Es laborable")
    case _:
        print("No es un dia")


