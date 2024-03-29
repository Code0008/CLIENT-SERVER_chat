import socket

def conexion():

    host = 'localhost'
    port = 1234
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as c:
            c.connect((host,port))
            print(f'Conexion establecida con {host}')
            msg=b"eres pendejo"
            c.sendall(msg)
            r=c.recv(1024)
            if not r:
                  print(f'no nos envio nada el servidor {host}')
            else:
                  print(f'{r.decode()}')
    print('conexion cerrada')

conexion()