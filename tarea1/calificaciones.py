#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:


# Gemini prompt: Haz un código en python que capture las calificaciones
# de alumnos utilizando monadas

from typing import Generic
from typing import TypeVar

E = TypeVar("E")
T = TypeVar("T")


class Either(Generic[E, T]):
    """Clase Either que puede tener el valor de fallo o exito"""

    def __init__(self, value):
        self.value = value

    def bind(self, f):
        if isinstance(self.value, Failure):
            return self
        else:
            return f(self.value)


class Success(Generic[T]):
    def __init__(self, value: T):
        self.value = value


class Failure(Generic[E]):
    def __init__(self, value: E):
        self.value = value


def get_valid_grade(prompt: str) -> Either[str, float]:
    while True:
        try:
            grade = float(input(prompt))
            if 0 <= grade <= 10:
                return Success(grade)
            else:
                return Failure("La calificación debe estar entre 0 y 10.")
        except ValueError:
            return Failure("Por favor, ingrese un número válido.")


def calculate_average(grades: list[float]) -> Either[str, float]:
    if not grades:
        return Failure("No hay calificaciones para calcular el promedio.")
    return Success(sum(grades) / len(grades))


def principal() -> None:
    """
    Función principal del programa
    """
    # Ejemplo de uso
    grades = []
    while True:
        grade = get_valid_grade("Ingrese una calificación (o 'q' para salir): ")
        if isinstance(grade.value, Failure):
            print(grade.value.value)
        elif grade.value == "q":
            break
        else:
            grades.append(grade.value)

    average = calculate_average(grades).bind(
        lambda avg: Success(f"El promedio es: {avg:.2f}")
    )
    print(average.value if isinstance(average.value, Success) else average.value.value)


if __name__ == "__main__":
    principal()
