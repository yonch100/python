# Listas almacenan objeto mediante un orden definido con posibilidad de duplicarlos
# las listas son estructuras de datos mutables (se puede añadir, eliminar o modificar)

emptyList = []
lenguajes = ["python", "java", "C++"]
numbers = [1,2,3,4,5,6,7,8,9]
data = ['Tenerife', {'cielo': 'limpio', 'temp': 24}, 3718, (28.2933947, -16.5226597)]

print(emptyList)
print(lenguajes)
print(numbers)
print(data)

print("--------------------------------------------------------------------------2")

ciudades = ["saltillo", "monterrey", "guanajuato", "zacatecas"]
print(ciudades)

print("--------------------------------------------------------------------------3")
#para ccnvertir algo en una lista se hace de la siguiente manera
lenguaje = list("python")
print(lenguaje)

print("--------------------------------------------------------------------------4")
listaMandado = ["agua", "cafe", "azucar", "leche", "galletas"]
print(listaMandado)
#Para agregar im valor en la lista se usa:
listaMandado.append("vaso")
print(listaMandado)

print("--------------------------------------------------------------------------5")
listaColores = ["verde"]

for index in range(3):
    color = input("Que color que quiereas agregar: ")
    listaColores.append(color)

print(listaColores)

print("--------------------------------------------------------------------------6")

# combinacio de listas
shopping = ['Agua', 'Huevos', 'Aceite']
fruitshop = ['Naranja', 'Manzana', 'Piña']
print(shopping + fruitshop)

print("--------------------------------------------------------------------------7")
#Modificar una lista
frutas = ["Papoalla","Pera","Platano"]
frutas[0] = "Limon"
print(frutas)
