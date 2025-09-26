usario1 = input("Ingresa que opcion vas a sacar piedra , tijera o papel  Usario1 =>")
usario2 = input("Ingresa que opcion vas a sacar piedra , tijera o papel  Usario2 =>")


match usario1:
    case "piedra":
      if usario2 == "papel":
          print("Usario2 ha ganado ")
      else:
          print("Usario1 ha ganado ")
    case "tijera":
        if usario2 == "piedra":
            print("Usario2 ha ganado ")
        else:
            print("Usario1 ha ganado ")
    case "papel":
        if usario2 == "Tijera":
            print("Usario2 ha ganado ")
        else:
            print("Usario1 ha ganado ")


jug1 = input("Jugador 1 (piedra 🗿, papel 🧻, tijeras ✂️): ").lower()
jug2 = input("Jugador 2 (piedra 🗿, papel 🧻, tijeras ✂️  ): ").lower()

match (jug1, jug2):
    case (x, y) if x == y :
        print("Empate")
    case ("piedra", "tijeras") | ("tijeras", "papel") | ("papel", "piedra"):
        print("Jugador 1 gana")
    case ("tijeras", "piedra") | ("papel", "tijeras") | ("piedra", "papel"):
        print("Jugador 2 gana")
    case _:
        print("Jugada no válida")

