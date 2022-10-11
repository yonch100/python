class Alumno:

    #nombre = ""
    #calificacion = 0.0

    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def get_nombre(self):
        return self.nombre

    def get_calificacion(self):
        return self.calificacion

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_calificacion(self, calificacion):
        self.calificacion = calificacion

    def toString(self):
        print(f"El nombre del alumno es: {self.nombre} y su calificacion es: {self.calificacion}")

    def validarCalificacion(self, calificacion):
        if calificacion > 70:
            print("El Alumno esta Aprobado")
        else:
            print("El Alumno esta reprobado")

#-------------------------------------------------------------------------------------------------------

alumno1 = Alumno("juan", 69)

alumno1.set_nombre("Omar")
alumno1.set_calificacion(80)

print(alumno1.get_nombre())
print(alumno1.get_calificacion())

alumno1.validarCalificacion(80) #se puede poner el valor de la calif o bn el get > alumno1.get_calificacion()
#alumno1.validarCalificacion(alumno1.get_calificacion())




