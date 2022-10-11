'''
Dado el diccionario de ciudades y poblaciones ya visto, y suponiendo que estas ciudades son
las únicas que existen en el planeta, calcule el porcentaje de población relativo de cada una
de ellas con respecto al total.
'''
diccionarioCiudades = {
    "Tokyo": 38_140_000,
    "Delhi": 26_454_000,
    "Shanghai": 24_484_000,
    "Mumbai": 21_357_000,
    "Sao Paulo": 21_297_000
}

#Con este ciclo for se saca el total de la poblecion iterando en el diccionario por medio de los valores
totalPoblacion = 0
for iterador in diccionarioCiudades.values():
    totalPoblacion += iterador
print(f"El total de poblacion es: {totalPoblacion}")

print("CIUDAD --- PORCENTAJE DE POBLACION MUNDIAL")
for i, j in diccionarioCiudades.items():
    porcentaje = (j * 100) / 131732000
    #print(porcentaje)
    print(f"{i} ---- {porcentaje}")
