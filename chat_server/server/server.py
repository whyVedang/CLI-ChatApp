import socket,threading
from config import IP, PORT 
from handlers import handle_client


clients={}
hosts={}


def main():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen()
    print("Server is running")
    while True:
        client_socket,client_addr=server.accept()
        threading.Thread(target=handle_client,args=(client_socket,clients,hosts),daemon=True).start()

if __name__=='__main__':
    main()