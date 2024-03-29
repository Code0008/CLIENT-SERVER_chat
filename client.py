import socket
host='localhost'
port=1234

c =socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
c.connect((host, port))
print(f'conexion con {host} esta realizada con exito')
while True:
    resp = input("[+]Mensaje de enviar al servidor: ")
    c.send(resp.encode())
    svmessage= c.recv(1024).decode()
    print(f'MENSAJE RECIBIDO: {svmessage}')
        

