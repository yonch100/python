import pytest
class Calculadora():

    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        suma = self.num1 + self.num2
        return suma
        #print("el resultado de la suma es: ", suma)

    def restar(self):
        resta = self.num1 - self.num2
        return resta
        #print("el resultado de la resta es: ", resta)

    def multiplicar(self):
        if self.num1 >= 0 and self.num2 >= 0:
            multiplicacion = self.num1 * self.num2
            return multiplicacion
        else:
            return False
        #print("el resultado de la multiplicación es: ", multiplicacion)

    def dividir(self):
        divicion = self.num1 / self.num2
        return divicion
        #print("el resultado de la divición es: ", divicion)
