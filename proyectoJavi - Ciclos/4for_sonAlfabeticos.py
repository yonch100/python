
palabra = input("Ingresa la palabra a validar")

for iterador in palabra:
    if iterador.isalpha():
        continue
    else:
        print(f"{iterador} no es una letra")