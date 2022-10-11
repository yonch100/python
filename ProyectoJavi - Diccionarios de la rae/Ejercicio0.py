#cadena = input("Ingresa la cadena de texto con las ciudades y habitantes.")
cadena = "Tokio:2_500_000;CDMX:2_4569_009;Rio de Janeiro:560_0000"
cadena_partida = cadena.split(";")

diccionario = {}
total_poblacion = 0

for elem in cadena_partida:
    poblacion = int(elem.split(":")[1])
    total_poblacion += poblacion

for elem in cadena_partida:
    ciudad = elem.split(":")[0]
    poblacion = int(elem.split(":")[1])
    porcentaje = poblacion * 100 /total_poblacion
    diccionario[ciudad] = porcentaje

print(diccionario)