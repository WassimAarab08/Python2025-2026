import random
intentos = 4
flag = True
numero = random.randrange(0,10)
while flag and intentos > 0:
  numeroIntroducido = int(input("Ingresa numeros postivos  : "))
  if numeroIntroducido != numero:
    intentos = intentos - 1
  elif numeroIntroducido == numero:
      print("El numero ingresado es correcto")
      flag= False

if intentos <= 0:
  print("El numero era",numero)