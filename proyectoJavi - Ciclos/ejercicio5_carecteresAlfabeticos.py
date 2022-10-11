cadena = input("Ingresa la cadena a validar: ")

for i in cadena:
    if i.isalpha():
        continue
    else:
        print(f"El caracter: {i} de la cadena no es una letra")