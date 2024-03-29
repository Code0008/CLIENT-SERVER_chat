#conexion de tipo UDP
#El UDP es menos fiable pero funciona más rápido.
import socket


def UDPconexion():
    host ='localhost'
    port =1234

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host,port))
        print('SERVIDOR AL AIRE GAAA')
        while True:
            data, direc = s.recvfrom(1024)
            s.sendto('MENSAJE RECIDO WAZA'.encode(),)
            print(f'mensaje recibido de {direc}: {data.decode()}')

UDPconexion()
