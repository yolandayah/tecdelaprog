#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:

# Gemini prompt: Haz un código en python que capture las calificaciones
#                de alumnos utilizando monadas
# Se usó el código como ejemplo, se corrigió y se mejoró (tenia varios errores)


class Either:
    """Clase Either que puede tener el valor de fallo o exito"""

    def __init__(self, value):
        self.value = value

    def bind(self, f):
        """Función que me sirve como monada para las calificaciones"""
        if isinstance(self, Failure):
            return self
        else:
            return f(self.value)


class Success(Either):
    """Clase Exito
    Se usa cuando hay exito en la captura
    """

    def __init__(self, value):
        self.value = value


class Failure(Either):
    """Clase Fallo
    Se usa cuando hay un fallo en la captura
    """

    def __init__(self, value):
        self.value = value


def get_valid_grade(prompt: str) -> Either:
    """Obtiene los valores del teclado"""

    valor = input(prompt)

    # Verificamos si es "Q" o "q"
    if valor.lower() == "q":
        return Success(valor)

    try:
        grade = float(valor)
        if 0 <= grade <= 10:
            return Success(grade)
        else:
            return Failure("La calificación debe estar entre 0 y 10.")
    except ValueError:
        return Failure("Por favor, ingrese un número válido.")

    return Failure("Por favor, ingrese un número válido.")


def calculate_average(grades: list[float]) -> Either:
    """Función que calcula el promedio por medio de una monada either"""
    if not grades:
        return Failure("No hay calificaciones para calcular el promedio.")
    return Success(sum(grades) / len(grades))


def principal() -> None:
    """
    Función principal del programa
    """

    grades = []
    salir = False

    while not salir:
        grade = get_valid_grade("Ingrese una calificación (o 'q' para salir): ")

        if isinstance(grade, Failure):
            # Imprime el mensaje de error
            print(grade.value)
        elif grade.value == "q":
            salir = True
        else:
            grades.append(grade.value)

    average = calculate_average(grades).bind(
        lambda avg: Success(f"El promedio es: {avg:.2f}")
    )
    print(average.value if isinstance(average.value, Success) else average.value)


if __name__ == "__main__":
    principal()
