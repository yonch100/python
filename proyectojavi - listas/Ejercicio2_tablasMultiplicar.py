#ingresar un numero por teclado y guardar en una lista su tabla de multiplicar hasta el 10

numero = int(input("Capturar numero a multiplicar: "))
multiplicadores = [1,2,3,4,5,6,7,8,9,10]
#multiplicadores = ["a","b","c","d","e","f","g","h","i","j"]

resultadoMultiplicacion = []

for i in multiplicadores:
    resultado = numero * i
    cadena = f"{numero} * {i} = {resultado}"
    resultadoMultiplicacion.append(cadena)

print(resultadoMultiplicacion)
    #print(f"{numero} x {i} = {resultado}")