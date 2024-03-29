import socket

def star():
    host= 'localhost'
    port= 1234
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host,port))
        print(f'servidor {host} ACTIVO!')
        s.listen(1)
        con, adr= s.accept()
        with con:
            print(f'se conecto el cliente de ip {adr}')
            while True:
                data = con.recv(1024)
                if not data:
                    break
                else:
                    print(f'es la informacion del cliente {data.decode()}')
                    msg=b"\neltingling \n"
                    con.sendall(msg)
    print(f'conexion cerrada con {adr}')

star()