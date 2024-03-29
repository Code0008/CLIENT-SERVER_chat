import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addres = ('localhost', 1234)
client_socket.connect(server_addres)
try:
    msg=b"WAZAA"
    client_socket.sendall(msg)
    x = client_socket.recv(1024)    
    print(f'el server respondio {x.decode()}')
finally:
    client_socket.close()