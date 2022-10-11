'''
Escribir un programa en python qeu almacen las asignaturas de un curso en una lista
1.- preguntar al usuario la nota que ha sacado en cada asignatura
2.- elimine de la lista las asignaturas aprobadas
3 - al final del programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir
'''

listaAsignaturas = ["Mate", "Fisica", "Quimica", "Historia", "Lengua"]
listaMateriasARepetir = []

#for i in reversed(listaAsignaturas):
for i in listaAsignaturas:
    calificacion = int(input(f"Que calificacion obtuvo en {i}: ") )

    if calificacion < 70:
        listaMateriasARepetir.append(i)
    else:
        continue

print("Materias Que el alumno repetira")
print(listaMateriasARepetir)