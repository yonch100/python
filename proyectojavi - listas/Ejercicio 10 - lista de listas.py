entrada = [0,1,[2,3],4,[5,6,7],8,9,[10,11,12,13]]

listaAplanada = []

for i in entrada:
    if type(i) == list:
        for j in i:
            listaAplanada.append(j)
    else:
        listaAplanada.append(i)
print(listaAplanada)