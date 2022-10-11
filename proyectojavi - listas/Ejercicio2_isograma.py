# Determine si una cadena de texto dada es un ISOGRAMA , es decir, no se repite ninguna letra.
# Ejemplos: lumberjacks - backgrounds - downstream - six-years-old

#Creacion de la variable y asignacion de su valor
cadena = input("Captura la cadena de texto a validar: ")

#La candea se castea a una lista
listaCadena = list(cadena)

listaCadena2 = []
banderaisograma = 0

for i in listaCadena:
    if i in listaCadena2:
        #print("La palabra no es un isograma")
        banderaisograma += 1
        break
    else:
        if i.isalpha() == True:
            listaCadena2.append(i) #Se inserta la nueva letra a la segunda lista
            #print(listaCadena2) #Linea de control de la listaCadena2 - para ver que contiene la lista
            #print("La palabra es isograma")
        else:
            continue

if banderaisograma >= 1:
    print(f"{listaCadena} \nNO ES isograma")
else:
    print(f"{listaCadena} \nES isograma")


#car = '-'
3#print(car.isalpha())