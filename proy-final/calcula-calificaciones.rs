use std::fs::File;
use std::io::{BufRead, BufReader};
use std::sync::mpsc;
use std::thread;

fn main() {
    // Ruta del archivo CSV
    let file_path = "alumnos.csv";

    // Abrir el archivo
    let file = File::open(file_path).expect("No se pudo abrir el archivo");
    let reader = BufReader::new(file);

    // Crear un canal para comunicar los resultados
    let (tx, rx) = mpsc::channel();

    // Leer líneas del archivo
    let mut handles = vec![];
    for line in reader.lines().skip(1) { // Saltar la cabecera
        let line = line.expect("Error al leer una línea");
        let tx = tx.clone();

        // Crear un hilo para procesar cada alumno
        let handle = thread::spawn(move || {
            let fields: Vec<&str> = line.split(',').collect();
            let nombre = fields[0];
            let calificaciones_str = fields[2];

            let calificaciones: Vec<f64> = calificaciones_str
                .split('|')
                .filter_map(|x| x.parse::<f64>().ok())
                .collect();

            let promedio = if !calificaciones.is_empty() {
                calificaciones.iter().sum::<f64>() / calificaciones.len() as f64
            } else {
                0.0
            };

            tx.send((nombre.to_string(), promedio)).expect("Error al enviar el promedio");
        });

        handles.push(handle);
    }

    // Cerrar el canal de transmisión
    drop(tx);

    // Recibir y mostrar los resultados
    for result in rx {
        let (nombre, promedio) = result;
        println!("{}: Promedio = {:.2}", nombre, promedio);
    }

    // Esperar a que todos los hilos terminen
    for handle in handles {
        handle.join().expect("Error al unir el hilo");
    }
}

