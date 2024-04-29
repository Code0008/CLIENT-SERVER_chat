from tkinter import *
import socket
from tkinter.scrolledtext import ScrolledText
import threading
#///////////////////////////////
def send_message( clientsock,username,textwidget, entrywidget):
    message = entrywidget.get()
    clientsock.sendall(f'Username {username} > {message}'.encode())

    entrywidget.delete(0, END)
    textwidget.configure(state="normal")
    textwidget.insert(END, F" \n{username}>{message}")
    textwidget.configure(state="disabled")
    
#////////////////////////////////

def recv_message(clientsock, textwidget):
    while True:
        try: 
            message= clientsock.recv(1024).decode()
            if not message:
                break
            textwidget.configure(state='normal')
            textwidget.insert(END, message)
            textwidget.configure(state='disabled')
        except:
            break

#////////////////////////////////

def exit(clientsock, username, window):
    clientsock.sendall(f"[!] El usuario {username} se retir del chat".encode())
    clientsock.close()
    window.quit()
    window.destroy()

#////////////////////////////////
def listusernames(clientsock):
    clientsock.sendall("!usuarios".encode())
#////////////////////////////////


def client(): #Funcion Main
    host="localhost"
    port=1234

    clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsock.connect((host,port))
    username = input("INGRESE NOMBRE DE URUARIO: ")
    clientsock.sendall(username.encode())

    window= Tk()
    window.title("Chatmultiusuariowaza")
    
    
    textwidget = ScrolledText(window, state="disabled")
    textwidget.pack(padx=5,pady=5)


    frame = Frame(window, bg="red")
    frame.pack(fill=BOTH, expand=1, padx=5)

    entrywidget = Entry(frame)
    entrywidget.bind("<Return>", lambda event: send_message( clientsock, username, textwidget, entrywidget) )
    entrywidget.pack(side=LEFT, fill=BOTH, expand=1, padx=3, pady=3)

    botonenv = Button(frame, text="SEND", command=lambda : send_message(clientsock, username, textwidget, entrywidget))
    botonenv.pack(side=RIGHT, padx=3)
    
    botonuser = Button(frame, text="MOstrar kvros", command = lambda: listusernames(clientsock) )
    botonuser.pack()

    botonsalir = Button(frame, text="Salir del chat", command = lambda: exit(clientsock, username ,window) )
    botonsalir.pack()

    hiloconexionotrousuario = threading.Thread(target=recv_message, args=(clientsock, textwidget))
    hiloconexionotrousuario.daemon = True
    hiloconexionotrousuario.start()

    window.mainloop()
    clientsock.close()

if __name__ == "__main__":
    client()