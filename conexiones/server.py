import socket

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
adres=('localhost', 1234)
server_socket.bind(adres)
server_socket.listen(2)
while True:
    client_con, direc_client = server_socket.accept()
    mesage= client_con.recv(1024)
    client_con.sendall(f"el ting ling".encode())
    print(mesage.decode())
    client_con.close()