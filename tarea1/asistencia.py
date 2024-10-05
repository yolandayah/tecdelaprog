#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Ejemplo de una mónada para calcular el promedio de alumnos
"""


class Ponderacion:
    """Clase Ponderación

    Es usada para la saber lo que se va a calificar
    """

    def __init__(self, nombre: str, porcentaje: int, numero_maximo: int = 0):
        self.nombre = nombre
        self.porcentaje = porcentaje
        self.maximo = numero_maximo


class Calificacion:
    """Clase calificación

    Es usada para hacer los calculos de la calificación
    con la ponderación de cada elemento
    """

    def __init__(self):
        self.ponderaciones = []

    def add(self, ponderacion: Ponderacion):
        self.ponderaciones.append(ponderacion)


def principal():
    """
    Función principal del programa
    """
    cal = Calificacion

    print("Programa que te ayuda a calcular el promedio de un alumno\n\n")

    # Pregunta por los elementos que vamos a evaluar
    for elemento in ["Tareas", "Examenes", "Participación", "Asistencia"]:
        porcentaje = int(input(f"¿Cuánto es el porcentaje de las {elemento}?: "))
        num_max = 0

        if elemento != "Examenes":
            num_max = int(input(f"¿Cuántas {elemento} fueron?: "))

        cal.add(Ponderacion(elemento, porcentaje, num_max))

    # Variable para saber si queremos salir
    salir = False

    while not salir:
        print("\nIngresa las calificaciones de un alumno")
        print("   Si son Tareas pon cuantas tareas entrego.")
        print("   Si son Examenes pon su calificación")
        print("   Si es participación cuantas participaciones tubo")
        print("   Si son Asitencias pon cuantas asistencias tubo.")
        salir = True


if __name__ == "__main__":
    principal()
