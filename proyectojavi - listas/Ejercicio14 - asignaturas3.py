'''
Escribir un programa en python qeu almacen las asignaturas de un curso en una lista
1.- preguntar al usuario la nota que ha sacado en cada asignatura
2.- elimine de la lista las asignaturas aprobadas
3 - al final del programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir
'''

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []

for subject in subjects:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))
    if score >= 70:
        passed.append(subject)

for subject in passed:
    subjects.remove(subject)

print("Tienes que repetir " + str(subjects))

print(subjects)
print(passed)