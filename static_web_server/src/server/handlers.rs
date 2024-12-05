use std::fs;
use std::io::Write;
use std::path::{Path, PathBuf};

/// Despacha las peticiones de HTTP
pub fn handle_request(request: &[u8], stream: &mut impl Write, directory: &str) {
    let request = String::from_utf8_lossy(request);
    let request_line = request.lines().next().unwrap_or("");

    if let Some(file_path) = parse_request(request_line, directory) {
        if file_path.exists() && file_path.is_file() {
            respond_with_file(file_path, stream);
        } else {
            respond_with_404(stream);
        }
    } else {
        respond_with_400(stream);
    }
}

/// Parsea la petición HTTP GET y determina la ruta del archivo
fn parse_request(request_line: &str, directory: &str) -> Option<PathBuf> {
    if request_line.starts_with("GET ") {
        let parts: Vec<&str> = request_line.split_whitespace().collect();
        if parts.len() > 1 {
            let relative_path = parts[1].trim_start_matches('/');
            return Some(Path::new(directory).join(relative_path));
        }
    }
    None
}

/// Responde con un archivo
fn respond_with_file(file_path: PathBuf, stream: &mut impl Write) {
    if let Ok(contents) = fs::read(&file_path) {
        let mime_type = mime_guess::from_path(&file_path).first_or_octet_stream();
        let response = format!(
            "HTTP/1.1 200 OK\r\nContent-Type: {}\r\n\r\n",
            mime_type
        );
        stream.write_all(response.as_bytes()).unwrap();
        stream.write_all(&contents).unwrap();
    } else {
        respond_with_500(stream);
    }
}

/// Responde con un 404 Error no encontrado
fn respond_with_404(stream: &mut impl Write) {
    let response = "HTTP/1.1 404 NOT FOUND\r\n\r\n404 Not Found";
    stream.write_all(response.as_bytes()).unwrap();
}

/// Responde con un 400 Error mal request
fn respond_with_400(stream: &mut impl Write) {
    let response = "HTTP/1.1 400 BAD REQUEST\r\n\r\n400 Bad Request";
    stream.write_all(response.as_bytes()).unwrap();
}

/// Responde con un 500 Error interno del servidor
fn respond_with_500(stream: &mut impl Write) {
    let response = "HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\n500 Internal Server Error";
    stream.write_all(response.as_bytes()).unwrap();
}

