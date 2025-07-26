from config import ENCODER
from host import add_host,get_users_in_host, remove_user_from_all_hosts,add_user_to_host


def handle_client(client_socket,clients,hosts):
    username=client_socket.recv(1024).decode(ENCODER)
    client_socket.send(f"Welcome {username}! Type /help for commands.".encode(ENCODER))
    clients[username]=client_socket
    while True:
        try:
            mess=client_socket.recv(1024).decode(ENCODER)
            print(f"[{username}] received: {mess}")
            if not mess or mess.lower() == 'quit':
                break
            elif mess.startswith('#'):
                parts = mess.split(' ', 1)
                if len(parts) < 2:
                        client_socket.send(b"Invalid format. Use #host message\n")
                        return
                host = parts[0][1:]
                msg = parts[1][0:]
                broadcast(host, username, msg, hosts, clients)
            elif mess.startswith('@'):
                parts = mess.split(' ', 1)
                if len(parts) < 2:
                    return
                target = parts[0][1:]
                msg = parts[1][0:]
                dm(username, target, msg, clients)
            elif mess.startswith('/join'):
                host=mess.split(' ')[1].strip()
                client_socket.send(f"Joined host #{host}".encode(ENCODER))
                join_host(username,host,hosts)
            else:
                client_socket.send(b"Invalid command. Use @, #, or /join.\n")
        except Exception as e:
            print(f"Errrrrrrrrrr :{e}")
            break
    remove_user_from_all_hosts(username, hosts)
    del clients[username]
    client_socket.close()

def join_host(username, host_name, hosts):
    if host_name not in hosts:
        add_host(host_name,hosts)
    add_user_to_host(username,host_name,hosts)
    print(f"{host_name} joined by {username}")



def broadcast(host, sender_user, message, hosts, clients):
    print(f"[Broadcast] #{host} from {sender_user}: {message}")
    print(f"[Host Members] => {hosts.get(host)}")

    for username in get_users_in_host(host, hosts):
        print(f"[Trying to send to]: {username}")
        if username != sender_user and username in clients:
            try:
                clients[username].send(f"[#{host}/{sender_user}] {message}".encode(ENCODER))
                print(f"[Sent to]: {username}")
            except Exception as e:
                print(f"[Error sending to {username}]: {e}")



def dm(sender_user, target_user, message, clients):
    print(f"[DM] from {sender_user} to {target_user}: {message}")
    if target_user in clients:
        try:
            clients[target_user].send(f"DM from {sender_user} -> {message}".encode(ENCODER))
            print(f"[DM Sent to]: {target_user}")
        except Exception as e:
            print(f"[Error sending DM to {target_user}]: {e}")
    else:
        print(f"[DM Error] {target_user} not in clients")
        clients[sender_user].send("Target User Offline".encode(ENCODER))


##dm code logic

# def dm(sender_user, target_user, message, clients):
#     if target_user in clients:
#         clients[target_user].send(f"DM from {sender_user}->  {message}".encode(ENCODER) )
#     else:
#         clients[sender_user].send("Target User Offline".encode(ENCODER))

##broadcast code logic

# def broadcast(host, sender_user, message, hosts, clients):
#     if host not in hosts:
#         return
#     for username in get_users_in_host(host,hosts):
#         if username!=sender_user and username in clients:
#             clients[username].send(f"[#{host}/{sender_user}] {message}".encode(ENCODER))
