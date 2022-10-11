
#Es posible ingresar la palabra o hardodearla
#palabra = input("Ingresa la palabra a validar")
palabra = "Supercalifragilisticoespialidoso"
contadorVocales = 0

for iterador in palabra:
    if iterador=="a" or iterador=="e" or iterador=="i" or iterador=="o" or iterador=="u":
        contadorVocales += 1
    else:
        continue

print(f"El numero de vocales en la palabra {palabra} es {contadorVocales}")