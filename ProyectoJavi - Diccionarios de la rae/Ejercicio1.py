print("EJERCICIO 1-------------------------------------------------------------------------------------")
'''
Construya un diccionario partiendo de una cadena de texto con el siguiente formato:
<city>:<population>;<city>:<population>;<city>:<population>;....
'''

diccionarioCiudades = {
    "Mexico": 100_000,
    "USA": 300_000,
    "Canada": 175_000,
    "Argentina": 80_000,
    "Brasil": 100_000
}

print(diccionarioCiudades)

print("\nEJERCICIO 2-------------------------------------------------------------------------------------")
'''
Usando un diccionario, cuente el número de veces que se repite cada letra en una cadena de texto dada.
'''
cadena = "boom"
diccionarioPalabra = {}

for i in cadena:
    numeroDeVeces = cadena.count(i)
    diccionarioPalabra[i] = numeroDeVeces

print(diccionarioPalabra)

print("\nEJERCICIO 3-------------------------------------------------------------------------------------")