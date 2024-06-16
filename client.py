import socket

def start_client(host="127.0.0.1", port=65432):
    """Inicia el cliente de eco."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(b"saludo")
            data = s.recv(1024)
            print(f"Recibido {data!r}")
    except ConnectionError as e:
        print(f"Servidor rechazo la conexion: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    start_client()
