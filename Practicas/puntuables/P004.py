from unittest import case

from boltons.strutils import format_int_list

figura = int(input("Que figura quieres 1-Cudrado ,2-Rectangulo ,3-Triangulo ,4-Rombo ,5-Pentago ,6-Hexa , 7-Circulo ,8-Trapecio ,9-Paralelogramo"))

match figura:
   case 1:
       L1 = int(input("Escribe L1 del cuadrado ?"))
       print(f"El area es {L1*L1}")
       print(f"El perimetro es {L1+L1+L1*L1}")
   case 2:
        L1 = int(input("Escribe L1 del rectangulo ?"))
        L2 = int(input("Escribe L2 del rectangulo ?"))
        print(f"El area es {L1 * L2}")
        print(f"El perimetro es {L1 + L2 + L1 + L2}")
   case 3:
       L1 = int(input("Escribe L1 del triangulo ?"))
       B2 = int(input("Escribe B2 del triangulo ?"))
       print(f"El area es {L1 *B2/2 }")
       print(f"El perimetro es {L1 + L1 + L1}")
   case 4:
       L1 = int(input("Escribe L1 del Rombo ?"))
       print(f"El area es {L1 * L1 /2}")
       print(f"El perimetro es {L1 + L1 + L1 + L1}")
   case 5:
       L1 = int(input("Escribe L1 del pentago ?"))
       L2 = int(input("Escribe apotema del pentago ?"))
       print(f"El area es {L1 * L2 /2 }")
       print(f"El perimetro es {L1 *5}")

   case 6:
       L1 = int(input("Escribe L1 del hexa?"))
       L2 = int(input("Escribe apotema del hexa ?"))
       print(f"El area es {L1 * L2 / 2}")
       print(f"El perimetro es {L1 * 6}")
   case 7:
        L1 = int(input("Escribe L1 del circulo ?"))
        L2 = int(input("Escribe L2 del circulo ?"))
        print(f"El area es {3,14 * (L2**2)}")
