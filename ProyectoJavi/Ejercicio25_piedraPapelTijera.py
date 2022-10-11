JugadaUsr1 = input("Captura la jugada del usr 1: Piedra, Papel o tijera:\n").lower()
JugadaUsr2 = input("Captura la jugada del usr 2: Piedra, Papel o tijera:\n").lower()

if JugadaUsr1 == "piedra" and JugadaUsr2 == "papel":
    print("Usuario 1 pierde, Usuario2 GANA")
elif JugadaUsr1 == "piedra" and JugadaUsr2 == "tijera":
    print("Usuario 1 GANA, Usuario2 pierde")
elif JugadaUsr1 == "papel" and JugadaUsr2 == "piedra":
    print("Usuario 1 GANA, Usuario2 piedra")
elif JugadaUsr1 == "papel" and JugadaUsr2 == "tijera":
    print("Usuario 1 pierde, Usuario2 GANA")
elif JugadaUsr1 == "tijera" and JugadaUsr2 == "piedra":
    print("Usuario 1 pierde, Usuario2 GANA")
elif JugadaUsr1 == "tijera" and JugadaUsr2 == "papel":
    print("Usuario 1 GANA, Usuario2 pierde")
elif JugadaUsr1 == "piedra" and JugadaUsr2 == "piedra" or JugadaUsr1 == "papel" and JugadaUsr2 == "papel" or JugadaUsr1 == "tijera" and JugadaUsr2 == "tijera":
    print("Los usuarios empatan... :(")
elif JugadaUsr1 != "piedra" or JugadaUsr1 != "papel" or JugadaUsr1 != "tijera" and JugadaUsr2 != "piedra" or JugadaUsr2 != "papel" or JugadaUsr2 != "tijera":
    print("Error de captura... :(")
