import socket

def updconexion():
    host = 'localhost'
    port = 1234
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as e:
        e.sendto('tingling'.encode(),(host,port))
        x = e.recvfrom(1024)
        print(x.decode())
updconexion()