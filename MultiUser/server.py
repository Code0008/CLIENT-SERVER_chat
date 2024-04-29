import socket
import threading



def client_thread(sockc, clients,usernames):
    username = sockc.recv(1024).decode()
    usernames[sockc]=username

    for client in clients:
        if client is not sockc:
            client.sendall(f"\n Se unio al chat: {username}".encode())

    while True:
        try:
            messahge = sockc.recv(1024).decode()


            if messahge == "!usuarios":
                sockc.sendall(f"\n[+] Todos los usuarios son { ', '.join(usernames.values())}".encode())
                continue

            for client in clients:
                if client is not sockc:
                    client.sendall(f"\n{messahge}".encode())

        except Exception as e:
            break
        
    sockc.close()
    clients.remove(sockc)
    del clients[sockc]
#////////////////////////////////
def server(): # Funcion main
    host = "localhost"
    port= 1234
    serv= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Reutilizamos conexion
    serv.bind((host,port))
    serv.listen()

    clients = []
    usernames = {}

    while True:
        sockc, dire = serv.accept() 
        clients.append(sockc) #Agregamos su socket
        hilocliente = threading.Thread(target=client_thread, args=(sockc, clients, usernames)) #proceso de usuario
        hilocliente.deamon = True
        hilocliente.start()

if __name__=="__main__":  server()