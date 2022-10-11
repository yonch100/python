'''
Funciones
'''


# Creacion de una funcion
def saludar():
    print("Hello")


# aplicacion de la funcion
saludar()

print("2---------------------------------------------")
variable1 = int(input("captura un numero ya sea 0 o 1: "))


def numero():
    if variable1 == 1:
        print("Uno")
    else:
        print("Cero")


numero()

print("3---------------------------------------------")


def vacio():
    x = 0


print(vacio())

print("4---------------------------------------------")

def verasidad(validacion):
    if validacion:
        print(f"{validacion} is true")
    else:
        print(f"{validacion} is false")

validacion = bool(input("captura False o True: ") )
print(verasidad(validacion) )

print("5---------------------------------------------")


def sqrt(numero):
    return numeroRaiz ** (1 / 2)


numeroRaiz = int(input("captura un numero para obtener su raiz cuadrada: "))
print(sqrt(numeroRaiz))

print("6---------------------------------------------")
numero1 = int(input("captura el primer numero: "))
numero2 = int(input("captura el segundo numero: "))


def numeroMenor(numero1, numero2):
    if numero1 < numero2:
        return numero1
    else:
        return numero2


print(numeroMenor(numero1, numero2))


