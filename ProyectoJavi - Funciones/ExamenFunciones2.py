"""
Construir una funcion que permita hacer busqeuda de inmuebles en funcion de un presupuesto dado.

La funcion recibira como entrada la lista de inmuebles y un precio y devolvera otra lista con los inmuebles
cuyo precio sea menor o igual que el dado.

Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio del inmueble,
donde el precio de un inmueble se calcula con las siguiente formula en funcion de la zona

Zona A: Precio = (metro *1000 + habitaciones * 5000 + garaje *15000) * (1 - antiguedad / 100)
Zona B: Precio = (metro *1000 + habitaciones * 5000 + garaje *15000) * (1 - antiguedad / 100)*1.5
"""

def agregarPrecio(lista):
    """
    Esta funcion valida en que zona y si tiene o no garage el inmueble correspondiente y dependiendo de esos valores
    agrega un par nuevo a la lista: presio:000,000

    :param lista: recibe la lista de inmuebles
    :return: lista: devuelve la lista de inmuebles + el par de precio
    """
    print("Propiedades disponibles segun tu presupuesto")
    print("--------------------------------------------------------------------------------------------------------------------")
    for i in lista:

        if i['zona'] == "A" and i['garaje'] == True:  # CUANDO GARAGE ES TRUE
            antiguedad = 1 - (2022 - i["anio"]) / 100
            zonaAPrecio = ((i['metros'] * 1000) + (i['habitaciones'] * 5000) + (1 * 15000)) * antiguedad

            i["Presio"] = zonaAPrecio
        else:
            if i['zona'] == "A" and i['garaje'] == False:  # CUANDO GARAGE ES FALSE
                antiguedad = 1 - (2022 - i["anio"]) / 100
                zonaAPrecio = ((i['metros'] * 1000) + (i['habitaciones'] * 5000) + (0 * 15000)) * antiguedad

                i["Presio"] = zonaAPrecio
        #----------------------------------------------------------------------------------------------------------
            else:
                if i['zona'] == "B" and i['garaje'] == True:  # CUANDO GARAGE ES TRUE
                    antiguedad = (1 - (i["anio"] - 2022) / 100) * 1.5
                    zonaBPrecio = ((i['metros'] * 1000) + (i['habitaciones'] * 5000) + (1 * 15000)) * antiguedad

                    i["Presio"] = zonaBPrecio
                else:
                    if i['zona'] == "B" and i['garaje'] == False:  # CUANDO GARAGE ES TRUE:
                        antiguedad = (1 - (i["anio"] - 2022) / 100) * 1.5
                        zonaBPrecio = ((i['metros'] * 1000) + (i['habitaciones'] * 5000) + (0 * 15000)) * antiguedad

                        i["Presio"] = zonaBPrecio
    return lista


def busquedaInmuebles(func, presupuesto):
    """
    Esta funcion muestra

    :param func: recibe la funcion agregarPrecio
    :param presupuesto:
    :return:
    """
    for i in func:
        if i["Presio"] <= presupuesto:
            print(i)

"""
--------------------------------------------------------------------------------------------------------------
"""
listaInmuebles = [
    {'id': 1, 'anio': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'id': 2, 'anio': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'id': 3, 'anio': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'id': 4, 'anio': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'id': 5, 'anio': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

#respuesta = input("Quieres iniciar la busqueda de Propiedades Si/No ---> ").lower()

#while respuesta == "si":
presupuesto = int(input("Ingresa el presupuesto con el que cuentas --> "))
var = agregarPrecio(listaInmuebles)

busquedaInmuebles(var, presupuesto)
#respuesta = input("Quieres realizar una nueva busqeuda Propiedsiades Si/No ---> ").lower()
#print("Gracias por visitarnos!!!")

