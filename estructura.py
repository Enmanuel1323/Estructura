from modelos.estudiante import Presencial, Distancia
from modelos.grupo import Grupo

def main():
    grupo = Grupo("Grupo 1")

    while True:
        print("\n--- Menú ---")
        print("1. Agregar estudiante")
        print("2. Registrar notas")
        print("3. Mostrar calificaciones")
        print("4. Calcular porcentaje de aprobados")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            matricula = input("Matrícula: ")
            tipo = input("Tipo (presencial/distancia): ").strip().lower()
            if tipo == "presencial":
                estudiante = Presencial(nombre, matricula)
            elif tipo == "distancia":
                estudiante = Distancia(nombre, matricula)
            else:
                print("Tipo inválido.")
                continue
            resultado = grupo.agregar_estudiante(estudiante)
            print(resultado.message)

        elif opcion == "2":
            matricula = input("Ingrese la matrícula del estudiante: ")
            try:
                examen = float(input("Nota del examen: "))
                practica = float(input("Nota de la práctica: "))
            except ValueError:
                print("Error: las notas deben ser numéricas.")
                continue
            resultado = grupo.registrar_notas(matricula, examen, practica)
            print(resultado.message)

        elif opcion == "3":
            grupo.mostrar_calificaciones()

        elif opcion == "4":
            resultado = grupo.calcular_porcentaje_aprobados()
            if resultado.success:
                print(f"Porcentaje de aprobados: {resultado.data:.2f}%")
            else:
                print(resultado.message)

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()