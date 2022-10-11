entrada = []

bandera = True
while bandera:
    elem = input("Ingresa el elemento de la lista: ")
    entrada.append(elem)
    opcion = input("Quieres ingresar otro elemento? 1: Si 2: No")
    if opcion == "2":
        bandera = False

lista_aplanada = []

for i in entrada:
    if type(i) == list:
        for j in i:
            lista_aplanada.append(j)
    else:
        lista_aplanada.append(i)
print(lista_aplanada)