class Banco():

    def retirar(self, valor, saldo):
        if (valor < saldo):
            return False, saldo
        saldo = saldo - valor
        return True, saldo

    def depositar(self, valor, saldo):
        saldo = saldo + valor
        return True, saldo

    def consultarSaldo(self, saldo):
        return True, saldo