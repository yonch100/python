
# Se captura la frase
# se le aplica el metodo lower para pasar la frase a minusculas
frase = input("Ingresa una frase: ").lower()

# se ingresa la palabra que buscara dentro de la frase
# Se aplica el metodo lower para pasar la palabra capturada a minusculas
palabraABuscar = input("Que palabra buscaras dentro de la frase: ").lower()

# se asigna el numero de veces que se encuentra la palabra a la variable numeroDeVeces
numeroDeVeces = frase.count(palabraABuscar)

#Se imprime la palabra y el numero de veces que se muestra
print(f"La palabra '{palabraABuscar}' aparece: {numeroDeVeces} veces")