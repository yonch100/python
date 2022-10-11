import math

#Se captura el radio, se convierte en tipo float y lo asigna a la variable radio
radio = float(input("Captura el radio de la esfera: ") )
volumen = (4/3)*math.pi*radio**3

#Se realiza la impresion de la variable volumen con formato
print(f"El volumen de la esfera es: {volumen}")