
print("TORRE 1 -----------------------------------------------")
tamaño = int(input("Tamaño de la torre: "))
for index in range(1,tamaño):
    print("*" * index)



print("TORRE 2 -----------------------------------------------")
indexinvertido = 5
for index in range(1,10,2):
    print((" " * indexinvertido) + ("*" * index) )
    indexinvertido = indexinvertido -1

'''
base = eval(input("Inglesa un numero inpar para la base del triangulo: "))
for i in range(1,base + 1,2):
    print(('*' * (i)).center(base,' ') )
'''