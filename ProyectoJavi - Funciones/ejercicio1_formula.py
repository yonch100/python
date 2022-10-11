'''
ejericico 1
funcion en python que reprodusca:
f(x,y) = x al cuadrado + y al cuadrado
'''

def fxy(x,y):
    operacion = x**2 + y**2
    print(operacion)

numero1 = int(input("captura el primer numero: "))
numero2 = int(input("captura el segundo numero: "))
fxy(numero1,numero2)
