#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
"""
Ejemplo de una mónada para calcular el promedio de alumnos
"""


class Ponderacion:
    """Clase Ponderación

    Es usada para la saber lo que se va a calificar
    """

    def __init__(self, nombre: str, numero_maximo: int):
        self.nombre = nombre
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

    for elemento in ["Tareas", "Examenes", "Participación", "Asistencia"]:
        numero = int(input(f"¿Cuanto es el porcentaje de las {elemento}?"))
        cal.add(Ponderacion(elemento, numero))


if __name__ == "__main__":
    principal()
