import socket

host = 'localhost'
port = 1234
def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
        c.connect((host, port))

    while True:
        message = input("Ingrese mensaje a enviar al servidor: ")
        c.sendall(message.encode())

        if message.lower() == 'bye':
            break
        reciv = c.recv(1024)
        print(f"respuesta del servidor es: {reciv.decode()}")

client()
    