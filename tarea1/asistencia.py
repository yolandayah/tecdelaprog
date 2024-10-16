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

    def add(self, ponderacion: Ponderacion) -> None:
        """Agrega las ponderaciones de las calificaciones"""
        elemento = {
            "ponderacion": ponderacion,
            "calificacion": 0.0,
        }
        self.ponderaciones.append(elemento)

    def ponderaciones_validas(self) -> bool:
        """Valida que las ponderaciones sean de 100%"""

        suma = 0
        for elemento in self.ponderaciones:
            suma += elemento["ponderacion"].porcentaje

        return suma == 100

    def calcular_promedio(self) -> float:
        """Calcula el promedio de las calificaciones"""

        promedio = 0
        for elemento in self.ponderaciones:
            promedio += (
                elemento["ponderacion"].porcentaje / 100 * elemento["calificacion"]
            )

        return promedio


def principal() -> None:
    """
    Función principal del programa
    """
    cal = Calificacion()

    print("Programa que te ayuda a calcular el promedio de un alumno\n\n")

    # Pregunta por los elementos que vamos a evaluar
    for elemento in ["Tareas", "Examenes", "Participación", "Asistencia"]:
        porcentaje = int(input(f"¿Cuánto es el porcentaje de las {elemento}?: "))
        num_max = 0

        if elemento != "Examenes":
            num_max = int(input(f"¿Cuántas {elemento} fueron?: "))

        pon = Ponderacion(elemento, porcentaje, num_max)
        cal.add(pon)

    if not cal.ponderaciones_validas():
        print("Los porcentajes NO suman 100%")
        return

    # Variable para saber si queremos salir
    salir = False

    while not salir:
        print("\nIngresa las calificaciones de un alumno")
        print("   Si son Tareas pon cuantas tareas entrego.")
        print("   Si son Examenes pon su calificación")
        print("   Si es participación cuantas participaciones tubo")
        print("   Si son Asitencias pon cuantas asistencias tubo.")
        print("\n   Para salir, solo da enter en Tareas")

        # for cal

        salir = True


if __name__ == "__main__":
    principal()
