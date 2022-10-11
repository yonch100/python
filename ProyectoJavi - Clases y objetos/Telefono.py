class Telefono:

    def __init__(self, manufacturer, screenSize, numCores):
        self.__manufacturer = manufacturer
        self.__screenSize = float(screenSize)
        self.__numCores = numCores
        self.__estatus = 0
        self.__apps = []

# ------------------------------------------------------------------------------Get
    @property
    def manufacturer(self):
        #print("Llamada getManufacturer")
        return self.__manufacturer

    @property
    def screenSize(self):
        #print("Llamada getScreenSize")
        return self.__screenSize

    @property
    def numCores(self):
        #print("Llamada getNumCores")
        return self.__numCores

    @property
    def estatus(self):
        #print("Llamada estatus")
        return self.__estatus

    @property
    def apps(self):
        # print("Llamada a las apps")
        return self.__apps

#------------------------------------------------------------------------------set

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    @screenSize.setter
    def screenSize(self,screenSize):
        self.__screenSize = screenSize

    @numCores.setter
    def numcores(self, numCores):
        self.__numCores = numCores

    @estatus.setter
    def estatus(self, estatus):
        self.__estatus = estatus

    @apps.setter
    def apps(self, apps):
        self.__apps = apps

#------------------------------------------------------------------------------Metodos

    def prender(self):
        if self.__estatus == 1:
            print("El celular ya se encuentra prendido")
        else:
            self.__estatus = 1
            print("Se prendio el celular")


    def apagar(self):
        if self.__estatus == 0:
            print("El celular ya se encuentra apagado")
        else:
            self.__estatus = 0
            print("Se apago el celular")


    def instalarApps(self, app, estatus):
        if estatus == 1:
            if app not in self.__apps:
                # app = input("Escribe que aplicacion vas a instalar: ")
                print(f"La aplicacion {app} se esta instalanado......... Instalada")
                self.__apps.append(app)
            else:
                print("La aplicacion a instalar ya se encuentra en tu celular")
        else:
            print("Para instalar una aplicacion, necesitas encender tu celular")


    def desistalarApps(self,app, estatus):
        if estatus == 1:
            if app in self.__apps:
                # app = input("Escribe que aplicacion vas a desistalar: ")
                print(f"La aplicacion {app} se esta desinstalanado......... Desinstalada")
                self.__apps.remove(app)

            else:
                print("La aplicacion a desistalar no se encuentra en tu celulsar")
        else:
            print("Para desistalar una aplicacion, necesitas encender tu celular")


    def toString(self):
        print(f":::::Informacion del telefono:::::\nManufacturer: {self.__manufacturer}\nscreen size: {self.__screenSize}\nCores: {self.__numCores}\nStatus: {self.__estatus}\nApps: {self.__apps}")

#------------------------------------------------------------------- "MAIN"

telefono1 = Telefono("Xiaomi", 5.0, 2)

"""
#--------------------------------------Celular prendido/apagado
telefono1.toString()
telefono1.apagar()
telefono1.prender()
telefono1.toString()
telefono1.prender()

#--------------------------------------Celular instalar/desistalar

telefono1.prender()
telefono1.instalarApps("Faceobok",telefono1.estatus)
telefono1.toString()
telefono1.desistalarApps("Faceobok",telefono1.estatus)
telefono1.toString()

#--------------------------------------gets
print(telefono1.manufacturer)
print(telefono1.screenSize)
print(telefono1.numcores)

#--------------------------------------sets
telefono1.manufacturer = "apple"
telefono1.screenSize = 8
telefono1.numcores = 6

telefono1.toString()

telefono1.apagar()
telefono1.instalarApps("Faceobok",telefono1.estatus)
telefono1.instalarApps("twitter",telefono1.estatus)

telefono1.toString()

telefono1.desistalarApps("Facebook")
"""





