import socket
import threading

class ClienteHilo(threading.Thread):
    def __init__(self,socketuser, direction) -> None:
        super().__init__()
        self.socketuser=socketuser
        self.direction= direction
        print(f'el usuario con la direccion {direction}')
    def run(self):
        message=''
        while True:
            data= self.socketuser.recv(1024)
            message = data.decode()
            if message.lower().strip() == 'bye':
                break
            print(f'mensaje enviado por el cliente: {message.strip()}')
            self.socketuser.send(data)
        print(f'el cliente{self.direction} se ha desconectado')
        self.socketuser.close()

host= 'localhost' 
port=1234
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host,port))
    print("conexion inicializada")    

    while True:
        s.listen()
        socketuser, direction = s.accept()
        hilo = ClienteHilo(socketuser, direction)
        hilo.start()