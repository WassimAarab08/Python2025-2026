dia = int(input("Escribe el día de tu cumpleaños => "))
mes = input("Escribe el mes de tu cumpleaños => ").lower()

if (dia >= 21 and mes == "marzo") or (dia <= 19 and mes == "abril"):
    signo = "Aries"
elif (dia >= 20 and mes == "abril") or (dia <= 20 and mes == "mayo"):
    signo = "Tauro"
elif (dia >= 21 and mes == "mayo") or (dia <= 20 and mes == "junio"):
    signo = "Géminis"
elif (dia >= 21 and mes == "junio") or (dia <= 22 and mes == "julio"):
    signo = "Cáncer"
elif (dia >= 23 and mes == "julio") or (dia <= 22 and mes == "agosto"):
    signo = "Leo"
elif (dia >= 23 and mes == "agosto") or (dia <= 22 and mes == "septiembre"):
    signo = "Virgo"
elif (dia >= 23 and mes == "septiembre") or (dia <= 22 and mes == "octubre"):
    signo = "Libra"
elif (dia >= 23 and mes == "octubre") or (dia <= 21 and mes == "noviembre"):
    signo = "Escorpio"
elif (dia >= 22 and mes == "noviembre") or (dia <= 21 and mes == "diciembre"):
    signo = "Sagitario"
elif (dia >= 22 and mes == "diciembre") or (dia <= 19 and mes == "enero"):
    signo = "Capricornio"
elif (dia >= 20 and mes == "enero") or (dia <= 18 and mes == "febrero"):
    signo = "Acuario"
elif (dia >= 19 and mes == "febrero") or (dia <= 20 and mes == "marzo"):
    signo = "Piscis"

print(f"{dia} / {mes} es {signo}")
