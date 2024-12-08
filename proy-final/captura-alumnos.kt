import java.io.File
import java.util.*

// Clase para representar a un alumno
data class Alumno(val nombre: String, val edad: Int, val calificaciones: List<Double>) {
    fun promedio(): Double = if (calificaciones.isNotEmpty()) calificaciones.average() else 0.0
}

fun guardarEnCSV(listaAlumnos: List<Alumno>, nombreArchivo: String) {
    val file = File(nombreArchivo)
    file.printWriter().use { writer ->
        writer.println("Nombre,Edad,Calificaciones,Promedio")
        listaAlumnos.forEach { alumno ->
            val calificaciones = alumno.calificaciones.joinToString("|")
            writer.println("${alumno.nombre},${alumno.edad},$calificaciones,${"%.2f".format(alumno.promedio())}")
        }
    }
    println("Alumnos guardados en el archivo $nombreArchivo")
}

fun main() {
    val listaAlumnos = mutableListOf<Alumno>()
    val scanner = Scanner(System.`in`)

    while (true) {
        println("\nMenú:")
        println("1. Agregar alumno")
        println("2. Mostrar lista de alumnos")
        println("3. Calcular promedio general de calificaciones")
        println("4. Guardar alumnos en archivo CSV")
        println("5. Salir")
        print("Seleccione una opción: ")

        when (scanner.nextInt()) {
            1 -> {
                scanner.nextLine() // Consumir el salto de línea
                print("Ingrese el nombre del alumno: ")
                val nombre = scanner.nextLine()
                print("Ingrese la edad del alumno: ")
                val edad = scanner.nextInt()
                print("Ingrese el número de calificaciones: ")
                val numCalificaciones = scanner.nextInt()

                val calificaciones = mutableListOf<Double>()
                for (i in 1..numCalificaciones) {
                    print("Ingrese la calificación $i: ")
                    calificaciones.add(scanner.nextDouble())
                }

                val alumno = Alumno(nombre, edad, calificaciones)
                listaAlumnos.add(alumno)
                println("Alumno agregado correctamente.")
            }

            2 -> {
                if (listaAlumnos.isEmpty()) {
                    println("La lista de alumnos está vacía.")
                } else {
                    println("\nLista de alumnos:")
                    listaAlumnos.forEachIndexed { index, alumno ->
                        println("${index + 1}. ${alumno.nombre} (Edad: ${alumno.edad}, Promedio: ${"%.2f".format(alumno.promedio())})")
                    }
                }
            }

            3 -> {
                if (listaAlumnos.isEmpty()) {
                    println("No hay alumnos registrados para calcular el promedio.")
                } else {
                    val promedioGeneral = listaAlumnos.flatMap { it.calificaciones }.average()
                    println("El promedio general de calificaciones es: ${"%.2f".format(promedioGeneral)}")
                }
            }

            4 -> {
                if (listaAlumnos.isEmpty()) {
                    println("No hay alumnos para guardar en el archivo.")
                } else {
                    print("Ingrese el nombre del archivo (con extensión .csv, ejemplo alumnos.csv): ")
                    val nombreArchivo = scanner.next()
                    guardarEnCSV(listaAlumnos, nombreArchivo)
                }
            }

            5 -> {
                println("Saliendo del programa. ¡Hasta luego!")
                break
            }

            else -> println("Opción no válida. Intente de nuevo.")
        }
    }
}

