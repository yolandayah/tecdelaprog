/// importamos el servidor
mod server;
use std::env;

/// La función principal del programa

fn main() {
    let args: Vec<String> = env::args().collect();
    
    // Si no pasan 3 argumentos se sale del programa
    if args.len() < 3 {
        eprintln!("Como usarlo: {} <ADDRESS> <DIRECTORY>", args[0]);
        std::process::exit(1);
    }

    let address = &args[1];
    let directory = &args[2];

    let server = server::WebServer::new(address, directory);
    server.run();
}

