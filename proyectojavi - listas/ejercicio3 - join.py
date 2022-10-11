
#Se captura la fecha en la variable fecha
fecha = input("Caputra una fecha en formato dd/mm/aa: ")
#fecha = ["01/01/22", "02/02/22"]

#dividimos la fecha por el caracter /
fechadividida = fecha.split('/')

dia = fechadividida[1]
mes = fechadividida[0]
año = fechadividida[2]

#fecha = "-".join(fecha)

#se crea una lista para la fecha por separado
fechaLista = [dia, mes, año]

#Se realiza el join a la fecha para agregar el separador -
fecha2 = '-'.join(fechaLista)

#impresion de la fecha con su nuevo simbolo
print(fecha2)