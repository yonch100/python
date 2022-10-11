# Crear un programa que permita al usuario elegir un candidato por el cual votar las posibilidades son:
# el candidato A por el partido rojo
# el candidato B por el partido verde
# el candidato C por el partido azul
# Segun el candidato elegido se le debe imprimir un mensaje "Usted ha votado por el partido (color)
# si el usuario ingresa una opcion que no corresponda a ninguno de los candidatos disponibles. indicar "Opcion erronea"

opcion = input("Selecciona por cual candidato quieres votar: \nOpcion A: Partido Rojo \nOpcion B: Partido verde \nOpcion C: Partido azul \n").lower()

if opcion == "a":
    print("Usted a votado por el partido Rojo")
elif opcion == "b":
    print("Usted a votado por el partido Verde")
elif opcion == "c":
    print("Usted a votado por el partido Azul")
else:
    print("Opcion erronea")