'''
write a python program to get the index of the first element whitch is greater than a specified element
'''

listaNumeros = [12,45,23,67,78,90,100,76,38,62,73,29,83]
#listaNumerosxTeclado = []

#Pedir numero para validar la lista
numero = int(input("Escribe el numero a comparar: ") )
index = 0

for i in listaNumeros:
    index = listaNumeros.index(i)
    if i > numero:
        print(f"{i} es mayor que {numero}")
        print(f"El numero esta en la posision {index}")
        break
    else:

        if index == len(listaNumeros)-1:
            print("Se llego al ultimo valor de la lista y no existe un valor mayor al ingresado")
        else:
            continue