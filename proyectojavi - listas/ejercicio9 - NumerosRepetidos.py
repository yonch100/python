'''
Escriba un programa en python qeu acepte una lista y genere otra lista eliminando los elementos duplicados consecutivos
Entrada: [0012344566678944]
Salida: [01234567894]

'''

listaNumeros = [0,0,1,2,3,4,4,5,6,6,6,7,8,9,4,4]

listaNuevaNumeros = []
for i in listaNumeros:
    if i not in listaNuevaNumeros:
        listaNuevaNumeros.append(i)

print(listaNuevaNumeros)