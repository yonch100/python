# Pedir cantidad de palabras
num_palabras = int(input("Ingrese la cantidad de palabras: "))

# Pedir la n cantidad de palabras ingresadas anteriormente
#Variable para iterar
iterador = 1
#Mientras que mi iterador sea menor o igual al número de palabras
lista_palabras = []

while iterador <= num_palabras:
    palabra = input(f"Digame la palabra {iterador} ")
    lista_palabras.append(palabra)
    iterador += 1
print(f"La lista creada es: {lista_palabras}")

palabra_eliminar = input("Dígame la palabra a eliminar: ")
num_veces = lista_palabras.count(palabra_eliminar)

for i in range(num_veces):
    lista_palabras.remove(palabra_eliminar)
#lista_string = " ".join(lista_palabras)

#print(f"La lista es ahora: {lista_string}")
print(f"La lista es ahora: {lista_palabras}")