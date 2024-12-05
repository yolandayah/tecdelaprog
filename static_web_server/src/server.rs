/// Importamos las librerias

use std::net::{TcpListener, TcpStream};
use std::sync::Arc;
use std::thread;
use std::io::Read;

mod handlers;

/// Creamos la estructura del servidor web
pub struct WebServer {
    address: String,
    directory: String,
}

impl WebServer {
    /// Se crea la instancia de un nuevo servidor Web
    pub fn new(address: &str, directory: &str) -> WebServer {
        WebServer {
            address: address.to_string(),
            directory: directory.to_string(),
        }
    }

    /// Se inicia el servidor y se despachan los archivos
    pub fn run(&self) {
        let listener = TcpListener::bind(&self.address)
            .expect("Fallo al asignar la dirección");
        let directory = Arc::new(self.directory.clone());

        println!("El servidor esta corriendo en {}", self.address);

        for stream in listener.incoming() {
            match stream {
                Ok(stream) => {
                    let directory = Arc::clone(&directory);
                    thread::spawn(move || {
                        handle_connection(stream, &directory);
                    });
                }
                Err(e) => eprintln!("Fallo la conexión: {}", e),
            }
        }
    }
}

/// Despacha una conexión de cliente
fn handle_connection(mut stream: TcpStream, directory: &str) {
    let mut buffer = [0; 1024];
    if let Ok(_) = stream.read(&mut buffer) {
        handlers::handle_request(&buffer, &mut stream, directory);
    } else {
        eprintln!("Error al leer de la conexión");
    }
}

