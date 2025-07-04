import config
def recieve(server):
    while True:
        try:
            mess=server.recv(1024).decode(config.ENCODER)
            if not mess:
                print(f"Server Disconnected")
                break
            else:
                print(f"\r\n{mess}\n> ", end="")
        except Exception as e:
            print(f"[Receive Error] {e}")
            break
        