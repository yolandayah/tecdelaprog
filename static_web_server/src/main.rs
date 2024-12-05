mod server;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    
    if args.len() < 3 {
        eprintln!("Usage: {} <ADDRESS> <DIRECTORY>", args[0]);
        std::process::exit(1);
    }

    let address = &args[1];
    let directory = &args[2];

    let server = server::WebServer::new(address, directory);
    server.run();
}

