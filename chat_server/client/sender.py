import config
def send(server):
    while True:
        try:
            mess=input('> ')
            server.send(mess.encode(config.ENCODER))
            if mess.lower=="quit":
                server.send(mess.encode(config.ENCODER))
                print("You have left the chat.")
                break
            if mess == "/help":
                print_help()
                continue
        except (ConnectionAbortedError, BrokenPipeError):
            print("[Connection closed]")
            break
    server.close()



def print_help():
    print("""
    ===== Chat Command Reference =====
    /join <host>     : Join or create a group chat
    #<host> <msg>    : Send message to group
    @<user> <msg>    : Send direct message
    quit             : Exit the chat
    /help            : Show this menu
    ==================================
    """)