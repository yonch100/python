
#Se crea la lista de la fecha
fechaLista = []

#se captura la fecha por separado
dia = input("Caputra una dia en formato dd: ")
fechaLista.append(dia)
mes = input("Caputra una mes en formato mm: ")
fechaLista.append(mes)
anio = input("Caputra una año en formato aa: ")
fechaLista.append(anio)

#Nueva variable para la impresion de la lista con su simbolo nuevo
fechaNueva = '-'.join(fechaLista)
print(fechaNueva)