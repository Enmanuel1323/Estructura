from modelos.operation_result import OperationResult

class Grupo:
    def __init__(self, nombre_grupo):
        self.nombre_grupo = nombre_grupo
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        return OperationResult("Estudiante agregado correctamente.", True, estudiante)

    def registrar_notas(self, matricula, examen, practica):
        for estudiante in self.estudiantes:
            if estudiante.get_matricula() == matricula:
                estudiante.registrar_calificaciones(examen, practica)
                return OperationResult("Notas registradas exitosamente.", True)
        return OperationResult("Estudiante no encontrado.", False)

    def mostrar_calificaciones(self):
        if not self.estudiantes:
            print("No hay estudiantes en este grupo.")
            return
        print(f"\nListado de calificaciones - Grupo {self.nombre_grupo}")
        for est in self.estudiantes:
            print(est.mostrar_informacion())

    def calcular_porcentaje_aprobados(self):
        if not self.estudiantes:
            return OperationResult("No hay estudiantes.", False)
        aprobados = sum(1 for est in self.estudiantes if est.esta_aprobado())
        porcentaje = (aprobados / len(self.estudiantes)) * 100
        return OperationResult("Porcentaje calculado correctamente.", True, porcentaje)