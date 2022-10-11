palabra = input("Ingresa una palabra: ").lower()
totalCaracteres = len(palabra)

totalA = palabra.count("a")
totalE = palabra.count("e")
totalI = palabra.count("i")
totalO = palabra.count("o")
totalU = palabra.count("u")

totalVocales = totalA + totalE + totalI + totalO + totalU
metrica = totalVocales * totalCaracteres
print(f"La metrica de la palabra es: {metrica}")