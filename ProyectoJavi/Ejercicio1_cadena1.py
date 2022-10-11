#Cadena
cadena = "Hola soy omar y estoy en el curso de python"

#Numero de caracteres en la cadena
print(len(cadena))

#Regresa una lista de las palabras con las que cuenta la cadena
print(cadena.split() )

#numero de palabas en una cadena
print(len(cadena.split() ) )

print("...................................................................")

#Cadena2
cadena2 = "Hola soy omar, y estoy feliz. Estoyen el curso de python!"

print(len(cadena2))
print(cadena2.split() )
print(len(cadena2.split() ) )


print("...................................................................")

#Invertir una cadena
print(cadena[::-1])


print("...................................................................")


cadena3 = "Python"
primer_caracter = cadena3[0]
ultimo_caracter = cadena3[-1]
medio_caracter = int(len(cadena3)/2)
print(str(primer_caracter) + str(medio_caracter) + str(ultimo_caracter))



