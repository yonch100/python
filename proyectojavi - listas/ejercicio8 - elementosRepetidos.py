'''
Escriba un programa en python que acepte una lista y elimine sus elementos duplicados
'''

listaPalabras = []
tamanioDeLista = int(input("Ingresa el número de elementos que tendrá la listade palabras: "))

#Se ingresan los elementos a la lista
for i in range(tamanioDeLista):
    listaPalabras.append(input("Ingresa la palabra a agrega: ") )
#Se imprime la lista de palabras completa
print(listaPalabras)

#Se crea una nueva lista para agregar las palabras sin las repetidas
listaNuevaPalabras = []
for i in listaPalabras:
    if i not in listaNuevaPalabras:
        listaNuevaPalabras.append(i)
#Nueva lista de palabras sin paralabras repetidas
print(listaNuevaPalabras)