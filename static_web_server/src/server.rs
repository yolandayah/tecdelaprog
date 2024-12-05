use std::net::{TcpListener, TcpStream};
use std::sync::Arc;
use std::thread;
use std::io::{Read, Write};
use std::fs;
use crate::handlers;

pub struct WebServer {
    address: String,
    directory: String,
}

impl WebServer {
    /// Creates a new instance of the WebServer.
    pub fn new(address: &str, directory: &str) -> WebServer {
        WebServer {
            address: address.to_string(),
            directory: directory.to_string(),
        }
    }

    /// Starts the server and handles incoming requests.
    pub fn run(&self) {
        let listener = TcpListener::bind(&self.address)
            .expect("Failed to bind to address");
        let directory = Arc::new(self.directory.clone());

        println!("Server is running at {}", self.address);

        for stream in listener.incoming() {
            match stream {
                Ok(stream) => {
                    let directory = Arc::clone(&directory);
                    thread::spawn(move || {
                        handle_connection(stream, &directory);
                    });
                }
                Err(e) => eprintln!("Connection failed: {}", e),
            }
        }
    }
}

/// Handles a single client connection.
fn handle_connection(mut stream: TcpStream, directory: &str) {
    let mut buffer = [0; 1024];
    if let Ok(_) = stream.read(&mut buffer) {
        handlers::handle_request(&buffer, &mut stream, directory);
    } else {
        eprintln!("Failed to read from connection");
    }
}

