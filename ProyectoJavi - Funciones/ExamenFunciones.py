"""
Construir una funcion que permita hacer busqeuda de inmuebles en funcion de un presupuesto dado.

La funcion recibira como entrada la lista de inmuebles y un precio y devolvera otra lista con los inmuebles
cuyo precio sea menor o igual que el dado.

Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio del inmueble,
donde el precio de un inmueble se calcula con las siguiente formula en funcion de la zona

Zona A: Precio = (metro *1000 + habitaciones * 5000 + garaje *15000) * (1 - antiguedad 7 100)
Zona B: Precio = (metro *1000 + habitaciones * 5000 + garaje *15000) * (1 - antiguedad 7 100)*1.5
"""

def calcularPrecio(lista, presupuesto):
    print("Propiedades disponibles segun tu presupuesto")
    print("--------------------------------------------------------------------------------------------------------------------")
    for i in listaInmuebles:

        if i['zona'] == "A" and i['garaje'] == True:  # CUANDO GARAGE ES TRUE
            zonaAPrecio = ((i['metros'] * 1000) + (i['habitaciones'] * 5000) + (i['garaje'] * 15000)) * (
                        1 - (i['anio'] - 2022) / 100)
            i["Presio"] = zonaAPrecio

            if i["Presio"] < presupuesto:
                print(i)
            else:
                pass
        elif i['zona'] == "A" and i['garaje'] == False:  # CUANDO GARAGE ES FALSE
            zonaAPrecio = ((i['metros'] * 1000) + (i['habitaciones'] * 5000)) * (1 - (i['anio'] - 2022) / 100)
            i["Presio"] = zonaAPrecio

            if i["Presio"] < presupuesto:
                print(i)
            else:
                pass

        #----------------------------------------------------------------------------------------------------------

        elif i['zona'] == "B" and i['garaje'] == True:  # CUANDO GARAGE ES TRUE
            zonaBPrecio = ((i['metros'] * 1000) + (i['habitaciones'] * 5000) + (i['garaje'] * 15000)) * (
                        1 - (i['anio'] - 2022) / 100) * 1.5
            i["Presio"] = zonaBPrecio

            if i["Presio"] < presupuesto:
                print(i)
            else:
                pass
        elif i['zona'] == "B" and i['garaje'] == False:  # CUANDO GARAGE ES TRUE:
            zonaAPrecio = ((i['metros'] * 1000) + (i['habitaciones'] * 5000)) * (1 - (i['anio'] - 2022) / 100)
            i["Presio"] = zonaAPrecio

            if i["Presio"] < presupuesto:
                print(i)
            else:
                pass
    print("\n")


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

respuesta = input("Quieres iniciar la busqueda de Propiedades Si/No ---> ").lower()
while respuesta == "si":
    presupuesto = int(input("Ingresa el presupuesto con el que cuentas --> "))
    calcularPrecio(listaInmuebles, presupuesto)

    respuesta = input("Quieres realizar una nueva busqeuda Propiedsiades Si/No ---> ").lower()



