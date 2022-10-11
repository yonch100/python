'''
Escribir un programa en python qeu almacen las asignaturas de un curso en una lista
1.- preguntar al usuario la nota que ha sacado en cada asignatura
2.- elimine de la lista las asignaturas aprobadas
3 - al final del programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir
'''

'''
Creacion de listas
listaAsignaturas almacena las materias que el alumno esta cursando
materiasPasadas, es una lista vacia donde se guardaran las materias que el alumno pase
'''
listaAsignaturas = ["Mate", "Fisica", "Quimica", "Historia", "Lengua"]
materiasPasadas = []

'''
ciclo for donde se ingresa las calificaciones de las materias y se evalua si tiene una calif > a 70
si es asi se guara la materia en una nueva lista
'''
for i in listaAsignaturas:
    calificacion = float(input(f"Que calificacion obtuvo en {i}: ") )
    if calificacion >= 70:
        materiasPasadas.append(i)

'''
ciclo for donde se evalua las materias existentes en la lista materiasPasadas y en base a la lista si existe
estas se eliminan de la lista general (listaAsignaturas)
'''
for i in materiasPasadas:
    listaAsignaturas.remove(i)

'''
Se muestra la lista de las materias que el alumno repetura
'''
print("Materias Que el alumno repetira")
print(listaAsignaturas)
