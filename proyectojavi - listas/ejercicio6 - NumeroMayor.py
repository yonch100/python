lista = []
num_elems = int(input("Ingresa el número de elementos que tendrá la lista: "))
for _ in range(num_elems):
    lista.append(int(input("Ingresa el número entero: ")))
mayor = lista[0]

for num in range(1, num_elems):
    if mayor <= lista[num]:
        mayor = lista[num]
print(mayor)