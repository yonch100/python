
telefono = input("ingresar telefono con el siguiente formato: +prefijo-numero-ext: ").split("-")

prefijo = telefono[0]
tel = telefono[1]
ext = telefono[2]

print("Telefono: " + tel)
