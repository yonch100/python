# Solicitar al usuario que ingrese los nomnres de 2 personas, las cuales se almacenarane en 2 variables
# A continuacion, imprimir "conicidencia" si los nombres de ambas personas comienzan con la misma letra o si
# terminan con la misma letra. si no es asi, imprimir "no hay conincidencia

nombre1 = input("Ingresa el nombre numero1: ").lower()
nombre2 = input("Ingresa el nombre numero2: ").lower()

if nombre1[0] == nombre2[0] or nombre1[-1] and nombre2[-1]:
    print("Coincidenca")
else:
    print("No hay Coincidencia")


print("\nNombres utilizados:")
print(nombre1)
print(nombre2)