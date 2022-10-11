import pytest
from unitarias.calculadora import Calculadora
resultado = 0

def test_validacion_suma():
    #setup
    calc1 = Calculadora(1, 2)
    #action
    resultado = calc1.sumar()
    #Assert
    assert resultado == 3, "El resultado es incorrecto, debe de ser 3"

def test_validacion_suma2():
    calc1 = Calculadora(-5, -5)
    resultado = calc1.sumar()
    assert resultado == -10, "El resultado es incorrecto, debe ser -10"


def test_validacion_resta1():
    calc1 = Calculadora(5,1)
    resultado = calc1.restar()
    assert resultado == 4, "El resultado es incorrecto, debe de ser 4"

def test_validacion_resta2():
    calc1 = Calculadora(-2,-2)
    resultado = calc1.restar()
    assert resultado == 0, "El resultado es incorrecto, debe de ser -4"


def test_validacion_Multi1():
    calc1 = Calculadora(10,3)
    resultado = calc1.multiplicar()
    assert resultado == 30, "El resultado es incorrecto, debe ser 30"


def test_validacion_Multi1():
    calc1 = Calculadora(-1,3)
    resultado = calc1.multiplicar()
    assert resultado == False, "Alguno de los numeros son negativos, no es posible multiplicar"



def test_validacion_divicion():
    calc1 = Calculadora(10,5)
    resultado = calc1.dividir()
    assert resultado == 2, "Resultado incorrecto. debe de ser 2"