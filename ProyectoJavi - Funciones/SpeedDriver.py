
def speedDriver(speed):
    puntos = int(input("Con cuantos puntos cuenta tu licencia: "))

    if speed <= 70:
        print("speed driver is ok")
    else:
        respuesta = int(input("¿El conductor manejo por ensima de 70kl/hr durante 5kl? --- Si:1/No=0"))
        if respuesta == 1:
            puntos = puntos + 1
            if puntos > 12:
                print("Licensia suspendida por jugarle al toreto! La familia es primero!")
            else:
                print("puntos:" + puntos)
        else:
            print("No te agregaron puntos a tu licencia pero tienes: " + puntos)


speed = int(input("Velocidad del conductor: "))
speedDriver(speed)