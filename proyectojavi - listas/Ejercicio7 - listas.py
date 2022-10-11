'''
Escribir un programa que acepte una lista de valores numericos y obtenga su valor maximo sin utilizar la funcion max( )
Entrada: [6,3,9,2,10,31,15,7]
Salida: 31
Reto*, usar los indices y el ciclo FOR (editado)
'''

print("SIN USAR LA FUNCION MAX-------------------------------------------------------------------------------------")
#SIN USAR LA FUNCION MAX

listaNumeros = []

tamanioDeLista = int(input("Ingresa el número de elementos que tendrá la lista: "))

for i in range(tamanioDeLista):
    listaNumeros.append(int(input("Ingresa el número entero: ")))
mayor = listaNumeros[0]

for num in range(1, tamanioDeLista):
    if mayor <= listaNumeros[num]:
        mayor = listaNumeros[num]
print(mayor)





'''
print("USANDO LA FUNCION MAX---------------------------------------------------------------------------------------")
#USANDO LA FUNCION MAX
listaNumeros2 = []
num_elems = int(input("Ingresa el número de elementos que tendrá la lista: "))

#El ciclo for recorrera el numero de veces que se capture en la linea de arriba
for i in range(num_elems):
    listaNumeros2.append(int(input("Ingresa el número a la lista: ")))

x = listaNumeros2
print(max(x))
'''
