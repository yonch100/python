
cadena1 = input("Ingresa la cadena numero 1: ")
cadena2 = input("Ingresa la cadena numero 2: ")

print(f"Se realizara el producto cartesiano con las cadenas {cadena1} y {cadena1}")

for it1 in cadena1:
    for it2 in cadena2:
        productoCartesiano = it1 + it2
        print(productoCartesiano)