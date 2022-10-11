'''
#Listas
listaNumeros1 = []
listaNumeros2 = []

#for para ingresar valores a la lista1
for iterador in range(0,4):
    valor = input(f"Ingresa el valor del indice {i} de la lista 1: ")
    listaNumeros1.append(valor)

#for para ingresar valores a la lista2
for iterador in range(0,4):
    valor = input(f"Ingresa el valor del indice {j} de la lista 2: ")
    listaNumeros2.append(valor)
'''

listaNumeros1 = ['4', '3', '8', '1']
listaNumeros2 = ['9', '2', '7', '3']

#Impresiones de listas
print(listaNumeros1)

operacion = 0
for i,j in zip(listaNumeros1,listaNumeros2):
    operacion += int(i) * int(j)

print(operacion)