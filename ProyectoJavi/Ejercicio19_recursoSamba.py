#Escriba un programa en python que acepta una ruta remota de recurso samba
# y lo separe en nombre(IP) del equipo y ruta
# entrada: //1.1.1.1/eoi/python
# salida: equipo = 1.1.1.1; ruta /eoi/python

#Se ingresa la ruta (recurso samba)
recursoSamba = input("Ingresa el recurso samba: ")

#se almacena la ruta sin los 2 primeros slash
rutacompleta = recursoSamba[2:]

#se identifica el primer slash
diagonal = rutacompleta.index("/")

#Se separan las rutas por el diagonal
ip = rutacompleta[:diagonal]
ruta = rutacompleta[diagonal:]

#se imprime la ip y la ruta
print(f"Equipo: {ip};\nruta: {ruta} ")

