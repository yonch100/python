nombre = input("Ingresa tu nombre: ").capitalize()
sexo = input("Ingresa tu sexo:\nM: Masculono\nF: Femenino\n").upper()

if sexo == "F" and nombre[0] <= "M" or sexo == "M" and nombre[0] <= "N":
    print("corresponde al grupo A")
else:
    print("corresponde al grupo B")