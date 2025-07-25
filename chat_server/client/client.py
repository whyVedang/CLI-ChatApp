import socket
import threading
import config
from reciever import recieve
from sender import send
def main():
    server,username=connect()
    threading.Thread(target=recieve,args=(server,),daemon=True).start()
    send(server)

def connect():
    username=input("Enter your username: ")
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.connect((config.IP,config.PORT))
    server.send(username.encode(config.ENCODER))
    return server,username

if __name__ == "__main__":
    main()