'''
Usando un diccionario, cuente el número de veces que se repite cada letra en una cadena de texto dada.
'''
#cadena = "boom"
cadena = input("Ingresa la cadea acontar")
diccionarioPalabra = {}

for i in cadena:
    numeroDeVeces = cadena.count(i)
    diccionarioPalabra[i] = numeroDeVeces

print(diccionarioPalabra)