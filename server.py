import socket


def start_server(host="127.0.0.1", port=65432):
    """Inicia el servidor de eco."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        print(f"Servidor escuchando en {host}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Conectado por {addr}")
                handle_client(conn)


def handle_client(conn):
    """Maneja la comunicación con el cliente."""
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
    except Exception as e:
        print(f"Error durante la comunicación con el cliente: {e}")
    finally:
        conn.close()
        print("Conexión cerrada")


if __name__ == "__main__":
    start_server()
