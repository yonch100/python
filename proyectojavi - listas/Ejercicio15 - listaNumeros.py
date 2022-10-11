
#tamanioDeLista = int(input("Ingresa el número de elementos que tendrá la listade palabras: "))
#listaNumeros1 = []

listaNumeros = [12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]

divicionLista = int(input("Ingresa el numero en el que se dividira la lista: ") )

'''
range(0, len(test_list), divicionLista) 
devuelve un rango de números que comienzan en 0 y terminan en "len(test_list)" con un paso de "divicionLista".
Por ejemplo, range(0, 15, 3) devolverá (23,90,100,62,83).

"test_list[i:i + divicionLista]" obtiene la parte de la lista que comienza en el índice i y termina exclusivamente en "i + divicionLista".
'''
listas = [
    listaNumeros[i:i+divicionLista]
    for i in range(0, len(listaNumeros), divicionLista)
]

print(listas)
