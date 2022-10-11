fecha = input("Ingresa la fecha de tu clase (Dia, DD/MM): ")

diaLetra = fecha[0:3].lower()
diaNumero = int(fecha[5:7])
mes = int(fecha[8:10])

if diaNumero < 31 and mes < 12:

    if diaLetra == "lun" or diaLetra == "mar" or diaLetra == "mie":
        examenes = input("¿Tomaras examenes el dia de hoy?: ")
        if examenes == "si":
            cantidadAprobados = float(input("¿Cuantos alumnos aprobaron?: "))
            cantidadReprobados = float(input("¿Cuantos alumnos reprobaron?: "))
            porcentajeAprobados = (cantidadAprobados * 100) / (cantidadAprobados + cantidadReprobados)
            print(f"La el porcentaje de alumnos aprobados es: {porcentajeAprobados}")
        else:
            print("No hubo examenes")


    elif diaLetra == "jue":
        porcentaje = float(input("Ingresa el porcentaje de asistensia a clase: "))
        if porcentaje >= 50:
            print("Asistio la mayoria")
        else:
            print("No asistió la mayoría")

    elif diaLetra == "vie":
        print("Curso dirigido a viajeros")
        if diaNumero == 1 and mes == 1 or diaNumero == 1 and mes == 7:
            print("Comienzo de ciclo")
            cantidadAlumnos = int(input("Ingresa la cantidad de alumnos que iniciaran el ciclo: "))
            costoPorAlumno = int(input("Ingresa el costo de inscripcion por alumno: "))
            costoTotal = cantidadAlumnos * costoPorAlumno
            print(f"El ingreso total por este ciclo es de: ${costoTotal}")
        else:
            print("Sin definicion... n_n")

else:
    print("Dia desconocido: dia es mayor a 31 o mes es mayor que 12")