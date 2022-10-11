# Escribir un programa que pregunte por consola por los productos de una cesta de la compra
# separados por comas,
# y muestre por pantalla cada uno de los productos en una linea distinta

elementosDeLaLista = int(input("Ingresa el numero de elementos de la lista: "))
productos = []

#while
i = 0
producto = []
while i < elementosDeLaLista:
    producto = str(input("Ingresa el producto a agragar: ") )
    productos.append(producto)
    i = i+1

while i < elementosDeLaLista:
    print(productos[0])
    i = i+1

#Impresion de la lista
#print(str(productos))

#listaCordata = str(productos).split(",")
#print(listaCordata)
