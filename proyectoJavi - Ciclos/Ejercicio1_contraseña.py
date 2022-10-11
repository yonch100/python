diaLetra = input("Ingresa el dia: Lunes,Martes,Miercoles,Jueves,Viernes: ").lower()
diaNumero = int(input("Ingresa el numero de dia 1 al 31: "))
mesNumero = int(input("Ingresa el numeor de mes: 1 al 12: "))

if diaNumero <= 31 and mesNumero <= 12:

    if diaLetra == "lunes" or diaLetra == "martes" or diaLetra == "miercoles":
        examenes = input("¿Tomaras examenes el dia de hoy?: ")
        if examenes == "si":
            cantidadAprobados = float(input("¿Cuantos alumnos aprobaron?: "))
            cantidadReprobados = float(input("¿Cuantos alumnos reprobaron?: "))
            porcentajeAprobados = (cantidadAprobados * 100) / (cantidadAprobados + cantidadReprobados)
            porcentajeAprobados = round(porcentajeAprobados,2)
            print(f"La el porcentaje de alumnos aprobados es: {porcentajeAprobados} %")
        else:
            print("No hubo examenes")

    elif diaLetra == "jueves":
        porcentaje = float(input("Ingresa el porcentaje de asistensia a clase: "))
        if porcentaje >= 50:
            print(f"Asistio la mayoria: {porcentaje} %")
        else:
            print(f"No asistió la mayoría: {porcentaje} %")

    elif diaLetra == "viernes":
        print("Curso dirigido a viajeros")
        if diaNumero == 1 and mesNumero == 1 or diaNumero == 1 and mesNumero == 7:
            print("Comienzo de ciclo")
            cantidadAlumnos = int(input("Ingresa la cantidad de alumnos que iniciaran el ciclo: "))
            costoPorAlumno = int(input("Ingresa el costo de inscripcion por alumno: "))
            costoTotal = cantidadAlumnos * costoPorAlumno
            print(f"El ingreso total por este ciclo es de: ${costoTotal}")
        else:
            print("Sin definicion... n_n")
    else:
        print("Dia Erroneo, capturar nuevamente")
else:
    print("Dia desconocido: dia es mayor a 31 o mes es mayor que 12")