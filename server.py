import socket
host='localhost'
port=1234
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    print(f'EL SERVIDOR ({host}) ESTA AL AIRE!')
    while True:
        s.listen(4)
        socketu,adree = s.accept()
        saludo = b"HOLA USUARIO"
        socketu.sendall(saludo)
        while True:
            user_message= socketu.recv(1024)
            print(f'\nmensaje recibd del cliente:{user_message.decode()}')
            if user_message.decode().lower() == 'cerrar':
                break
            resp=input("\n[+]Ingrese mensaje al cliente: ").encode()
            socketu.send(resp)



        
