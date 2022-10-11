'''
Para crear un diccionario es con llaves
'''

diccionario1 = {}

listaCompras = {
    "cafe": 10,
    "azucar": 20,
    "leche": 30,
    "agua": 40
}
'''
Diccionario apartir de una llave
dict([a1,b2])
{a:1,b:2}

Diccionario a partir de una tupla de cadenas de texto
dict((a1,b2))
{a:1,b:2}

Diccionario a partir de una lista de listas
dict([[a,1],[b,2]])
{a:1,b:2}
'''



print("1-------------------------------------------------------------------------------------")
#Impresion del diccionario
print(listaCompras)

#acceder a un valor del deccionario
print(listaCompras["cafe"] )

# con get sprint(listaCompras["cafe"])i existe devuelve el valor en caso contrario regresa NONE(Null)
print(listaCompras.get("agua") ) #40
print(listaCompras.get("cuchara")) #none

#Si el primer parametro no existe, el segundo esta para mostrarse
print(listaCompras.get("programacion", "No disponible") )




print("2-------------------------------------------------------------------------------------")
"""
Agregar valor a diccionario
Modificar valor a diccionario
"""
listaCompras["taza"] = 100
listaCompras["agua"] = 50
listaCompras["clavel"] = 50

#Impresion del diccionario
print(listaCompras)




print("3-------------------------------------------------------------------------------------")
"""
Existensia de un valor en el diccionario
esto es con in o not in
"""
print("taza esta en el diccionario listaCompras")
print("taza" in listaCompras)




print("4 Formas de obtener los valores o llaves-----------------------------------------------------------------------")
"""
Obtener datos del diccionario
"""
print(listaCompras.keys()) #obtener las llaves
print(listaCompras.values()) #Obtener los valores
print(listaCompras.items()) #obtener los pares del diccionario - regresa la lista en tuplas

print(len(listaCompras)) #longitud del diccionario


print("5 Iterar en un diccionario-------------------------------------------------------------------------------------")

for iterador in listaCompras.keys():
    print(iterador)

for iterador in listaCompras.values():
    print(iterador)

for i, j in listaCompras.items():
    print(f"{i}: {j}")

print("6 Convinar diccionarios----------------------------------------------------------------------------------------")

diccionarioTerminos = {
    "bifronte": "De dos frentes o caras",
    "ejuiciar": "someter una cuestion a examen"
}

diccionarioTerminos2 = {
    "anarcoide": "que tiende al desorden",
    "montuvio": "campesino de la costa"
}

#Se unen los diccionarios
print(diccionarioTerminos|diccionarioTerminos2) #union de los diccionarios

diccionarioTerminos.update(diccionarioTerminos2) # actualizacion de los disccionarios por medio de update
print(diccionarioTerminos)

print("7 Borrar elementos----------------------------------------------------------------------------------------")

diccionarioTerminos3 = {
    "valor1": "uno",
    "valor2": "dos",
    "valor3": "tres",
    "valor4": "cuatro",
    "valor5": "cinco"
}

del(diccionarioTerminos3["valor1"] )
diccionarioTerminos3.pop("valor4") # si la clave a extraer con pop no existe marca error

print(diccionarioTerminos3)


'''
    letra = i[0]
    if letra in salida:
        salida[letra].append(i)
    else:
        salida[letra] = i
    print(salida)
'''





