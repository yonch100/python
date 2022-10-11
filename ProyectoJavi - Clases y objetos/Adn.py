class Adn:

    #Atributos de clase
    #4 atributos de clase, cada uno representando una base nitrogenada con su valor como caracter
    adenina = 'A'
    timina = 'T'
    guanina = 'G'
    citosina = 'C'

    #Constructor que recibe una secuencia de caracteres (base)
    def __init__(self, secuenciaADN1, secuenciaADN2):
        self.secuenciaADN1 = secuenciaADN1
        self.secuenciaADN2 = secuenciaADN2

    def __str__(self):
        return f"Secuencia de ADN: {self.secuenciaADN}"




    @property
    def adenina(self):
        return (self.adenina)

    @property
    def timina(self):
        return (self.timina)

    @property
    def guanina(self):
        return (self.guanina)

    @property
    def citosina(self):
        return (self.citosina)

    @adenina.setter
    def adenina(self, adenina):
        self.adenina = adenina

    @timina.setter
    def timina(self, timina):
        self.timina = timina

    @guanina.setter
    def guanina(self, guanina):
        self.guanina = guanina

    @citosina.setter
    def citosina(self, citosina):
        self.citosina = citosina






    def calcularBaseA(self, secuenciaDeADN1, secuenciaDeADN2):
        """
        Metodo que calcula el numero total de ADENINA una de las bases presentes en la secuencia dada
        :param secuenciaADN:
        :return: int: CantidadDeBase
        """
        cadena = secuenciaDeADN1 + secuenciaDeADN2
        cantidadDeBaseA = 0
        #base = input("Ingresa la base nitrogenada a calcular ").upper()
        base = "A"
        for i in cadena:
            if base == i:
                cantidadDeBaseA += 1
            else:
                continue
        #print("La cantidad de ADENINA: ")
        return cantidadDeBaseA

    def calcularBaseG(self, secuenciaDeADN1, secuenciaDeADN2):
        """
        Metodo que calcula el numero total de GUANINA una de las bases presentes en la secuencia dada
        :param secuenciaADN:
        :return: int: CantidadDeBase
        """
        cadena = secuenciaDeADN1 + secuenciaDeADN2
        cantidadDeBaseG = 0
        #base = input("Ingresa la base nitrogenada a calcular ").upper()
        base = "G"
        for i in cadena:
            if base == i:
                cantidadDeBaseG += 1
            else:
                continue
        #print("La cantidad de GUANINA es: ")
        return cantidadDeBaseG

    def calcularBaseC(self, secuenciaDeADN1, secuenciaDeADN2):
        """
        Metodo que calcula el numero total de CITOSINA una de las bases presentes en la secuencia dada
        :param secuenciaADN:
        :return: int: CantidadDeBase
        """
        cadena = secuenciaDeADN1 + secuenciaDeADN2
        cantidadDeBaseC = 0
        #base = input("Ingresa la base nitrogenada a calcular ").upper()
        base = "C"
        for i in cadena:
            if base == i:
                cantidadDeBaseC += 1
            else:
                continue
        #print("La cantidad de CITOSINA es: ")
        return cantidadDeBaseC

    def calcularBaseT(self, secuenciaDeADN1, secuenciaDeADN2):
        """
        Metodo que calcula el numero total de TIMINA una de las bases presentes en la secuencia dada
        :param secuenciaADN:
        :return: int: CantidadDeBase
        """
        cadena = secuenciaDeADN1 + secuenciaDeADN2
        cantidadDeBaseT = 0
        #base = input("Ingresa la base nitrogenada a calcular ").upper()
        base = "T"
        for i in cadena:
            if base == i:
                cantidadDeBaseT += 1
            else:
                continue
        #print("La cantidad de TIMINA es: ")
        return cantidadDeBaseT





    def sumarSecuencias(self, secuencia1, secuencia2):
        adenina = ""
        timina = ""
        guanina = ""
        citosina = ""

        #secuencia1 = input("Ingresa la secuencia de ADN 1: ").upper()
        #secuencia2 = input("Ingresa la secuencia de ADN 2: ").upper()

        for i in secuencia1:
            if i == "A":
                adenina = adenina + "A"
            elif i == "T":
                timina = timina + "T"
            elif i == "G":
                guanina = guanina + "G"
            elif i == "C":
                citosina = citosina + "C"
            else:
                print("Se agrego una base desconosida")

        for i in secuencia2:
            if i == "A":
                adenina = adenina + "A"
            elif i == "T":
                timina = timina + "T"
            elif i == "G":
                guanina = guanina + "G"
            elif i == "C":
                citosina = citosina + "C"
            else:
                print("Se agrego una base desconosida")

        sumaBases = str(adenina + timina + guanina + citosina)
        print(f"La suma de las secuencias es: {sumaBases}")



    def porcentajeBases(self, a,g,t,c):

        total = a + g + t + c

        porcentajeAdenina = (a / total) * 100
        porcentajeGuanina = (g / total) * 100
        porcentajeTimina = (t / total) * 100
        porcentajeCitosina = (c / total * 100)

        print(f"% de Adenina: {porcentajeAdenina}")
        print(f"% de guanina: {porcentajeGuanina}")
        print(f"% de Timina: {porcentajeTimina}")
        print(f"% de Citosina: {porcentajeCitosina}")



    def MultiplicacionSecuencias(self,secuencia1, secuencia2):




    def toString (self):
        return (f"Secuencia de ADN: {self.secuenciaADN}")




#----------------------------------------------------------------------------------------------------

#Se captura la secuencia de bases y se guardan en las variables
secuenciaDeADN1 = input("Ingresar la secuencia de ADN1: ").upper()
secuenciaDeADN2 = input("Ingresar la secuencia de ADN2: ").upper()


#Se crean el objetos
adn1 = Adn(secuenciaDeADN1, secuenciaDeADN2)
#adn2 = Adn(secuenciaDeADN2)

#EJERCICIO 2
print("\n2.-Cantidad de bases nitrogenadas en las secuentas")
print(f"Adenina: {adn1.calcularBaseA(secuenciaDeADN1, secuenciaDeADN2)}" )
print(f"Guanina: {adn1.calcularBaseG(secuenciaDeADN1, secuenciaDeADN2)}" )
print(f"Citosina: {adn1.calcularBaseC(secuenciaDeADN1, secuenciaDeADN2)}" )
print(f"Timina: {adn1.calcularBaseT(secuenciaDeADN1, secuenciaDeADN2)}" )

#EJERCICIO 3
print("\n3.-Suma de las secuencias")
adn1.sumarSecuencias(secuenciaDeADN1,secuenciaDeADN2)

#EJERCICIO 4
print("\n4.-Porcentaje de las secuentas")
a = adn1.calcularBaseA(secuenciaDeADN1, secuenciaDeADN2)
g = adn1.calcularBaseG(secuenciaDeADN1, secuenciaDeADN2)
c = adn1.calcularBaseC(secuenciaDeADN1, secuenciaDeADN2)
t = adn1.calcularBaseT(secuenciaDeADN1, secuenciaDeADN2)
adn1.porcentajeBases(a,g,t,c)

#EJERCICIO 5
print("\n5.-Multiplicacion de las secuentas")




