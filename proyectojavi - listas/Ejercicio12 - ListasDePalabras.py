'''
Escriba un programa que permita crear 2 listas de palabras
a continuacion escriba las sigientes listas en las que deben de haber repeticiones

Lista de palabras que:
aparecen en las 2 listas
aparecen en la primera lista pero no en la seguntda
aparecen en la segunda lista pero no en la primera
aparecen en ambas listas
'''

listaNombres1 = []
listaNombres2 = []

tamanioDeLista1 = int(input("Ingresa el tamaño que tendra la LISTA DE NOMBRES 1: "))
tamanioDeLista2 = int(input("Ingresa el tamaño que tendrá la LISTA DE NOMBRES 2: "))

for i in range(tamanioDeLista1):
    nombre1= input(f"Lista 1: Captura en nombre de la persona en la posicion {i}: ")
    listaNombres1.append(nombre1)
    #listaNombres1.append(input(f"Captura en nombre de la persona en la posicion {i}: "))

for j in range(tamanioDeLista2):
    nombre2 = input(f"Lista 2: Captura en nombre de la persona en la posicion {j}: ")
    listaNombres2.append(nombre2)
    #listaNombres1.append(input(f"Captura en nombre de la persona en la posicion {i}: "))

#Lineas de control - impresion de la lista
print(listaNombres1)
print(listaNombres2)


'''
------------------------------------------------------------------aparecen en las 2 listas
'''
aparecenEnLas2 = []

for i in listaNombres1:
    if i in listaNombres2:
        aparecenEnLas2.append(i)

print("\nNombres que Aparece en las 2 listas")
print(aparecenEnLas2)


'''
------------------------------------------------------------------aparecen en la primera lista pero no en la seguntda
'''
aparecenenla1 = []

for i in listaNombres1:
    if i not in listaNombres2:
        aparecenenla1.append(i)

print("\nNombres que Aparece en la primera lista pero no en la segunda")
print(aparecenenla1)

'''
------------------------------------------------------------------aparecen en la segunda lista pero no en la primera
'''
aparecenenla2 = []

for i in listaNombres2:
    if i not in listaNombres1:
        aparecenenla2.append(i)

print("\nNombres que Aparece en la segunda lista pero no en la primera")
print(aparecenenla2)


'''
------------------------------------------------------------------Todas las palabras
'''
todasLasPalabras = []
todasLasPalabras = listaNombres1 + listaNombres2
print("\nContenido de las 2 listas juntas")
print(todasLasPalabras)
