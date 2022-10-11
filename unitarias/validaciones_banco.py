import pytest
from unitarias.banco import Banco

banco1 = Banco()
def test_depositar_efectivo():
    banco1.depositar(100,101)

def test_retirar_efectivo():
    banco1.retirar(100,0)

