# Determine si una cadena de texto dada es un isograma, es decir, no se repite ninguna letra.

palabra = input("Ingresar la palabra a validar: ")

#convertir cadena en lista
listaPalabra = list(palabra)
#impresion de la lista
print(listaPalabra)
indice = 0
for i in listaPalabra:
    if listaPalabra.count(i) >= 2:
        print("La Palbra ES Isograma")
    else:
        print("La Palbra NO ES Isograma")

