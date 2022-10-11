'''
escribir una funcion que dado un numero de DNI, retorne TRUE si el numero es valido y FALSO si no lo es
DNI valido entre 7 y 8  digitos
'''

def dni(identificacion):
    if len(identificacion) == 7 or len(identificacion) == 8:
        return True
    else:
        return False

identificacion = input("captura numero de DNI: ")
print(dni(identificacion) )