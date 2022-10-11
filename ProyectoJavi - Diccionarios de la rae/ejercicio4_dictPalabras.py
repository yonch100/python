listaPalabras = ["mesa","movil", "barco", "coche", "avion", "bandeja", "casa", "monitor", "carrera", "arco" ]
dictPorPalabra = {}

for i in listaPalabras:
    primerLetra = i[0]

    if primerLetra in dictPorPalabra:
        #Para agregar valor al dic ---- Diccionario [key] = value
        dictPorPalabra[primerLetra].append(i)
    else:
        dictPorPalabra[primerLetra] = [i]

print(dictPorPalabra)