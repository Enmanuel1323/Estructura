from abc import ABC, abstractmethod

class Estudiante(ABC):
    def __init__(self, nombre, matricula):
        self._nombre = nombre
        self._matricula = matricula
        self._calificaciones = [0.0, 0.0]

    def registrar_calificaciones(self, examen, practica):
        self._calificaciones = [examen, practica]

    @abstractmethod
    def calcular_nota_final(self):
        pass

    def mostrar_informacion(self):
        return f"Nombre: {self._nombre}, Matrícula: {self._matricula}, Nota Final: {self.calcular_nota_final():.2f}"

    def esta_aprobado(self):
        return self.calcular_nota_final() >= 70

    def get_matricula(self):
        return self._matricula

class Presencial(Estudiante):
    def calcular_nota_final(self):
        return self._calificaciones[0] * 0.7 + self._calificaciones[1] * 0.3

class Distancia(Estudiante):
    def calcular_nota_final(self):
        return self._calificaciones[0] * 0.5 + self._calificaciones[1] * 0.5