use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};
use std::fs;
use std::thread;

fn handle_client(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    let _ = stream.read(&mut buffer).unwrap();

    let get = b"GET /";
    if !buffer.starts_with(get) {
        println!("Invalid request");
        return;
    }

    let filename = std::str::from_utf8(&buffer[5..]).unwrap().trim();
    let filepath = format!("public/{}", filename);

    let mut file = match fs::File::open(filepath) {
        Ok(file) => file,
        Err(_) => {
            let _ = stream.write(b"HTTP/1.1 404 Not Found\r\n\r\n").unwrap();
            return;
        }
    };

    let mut response = format!("HTTP/1.1 200 OK\r\nContent-Length: {}\r\n\r\n", file.metadata().unwrap().len());
    stream.write_all(response.as_bytes()).unwrap();

    std::io::copy(&mut file, &mut stream).unwrap();
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                thread::spawn(|| {
                    handle_client(stream);
                });
            }
            Err(e) => {
                eprintln!("Error: {}", e);
            }
        }
    }
}
