import random
intentos = 6
flag = True
numero = random.randrange(0,3)
while flag and intentos > 0:
  numeroIntroducido = int(input("Ingresa numeros postivos  : "))
  if numeroIntroducido != numero:
    intentos = intentos - 1
  elif numeroIntroducido == numero:
      print("El numero ingresado es correcto")
      flag= False

if intentos <= 0:
  print("El numero era",numero)



