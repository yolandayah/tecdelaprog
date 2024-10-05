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
    pass


def principal():
    """
    Función principal del programa
    """
    print("Programa que te ayuda a calcular el promedio de un alumno\n\n")

    numero = int(input("¿Cuanto es el porcentaje de las Tareas?"))

    print(numero)


if __name__ == "__main__":
    principal()
