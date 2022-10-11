def palindromo(palabra):
    #palabraSinEspacios = list(palabra).remove(" ")
    #print(palabraSinEspacios)

    if str(palabra) == str(palabra)[::-1]:
        print("Es palindromo")
    else:
        print("No es palindromo")


palabra = input("Ingresa la palabra a validar: ")
palindromo(palabra)
