from config import ENCODER
from host import add_host,get_users_in_host, remove_user_from_all_hosts,add_user_to_host

def handle_client(client_socket,clients,hosts):
    pass

def join_host(username, host_name, hosts):
    if host_name not in hosts:
        add_host(host_name,hosts)
    add_user_to_host(username,host_name,hosts)
    print(f"{host_name} joined by {username}")

##dm code logic

def dm(sender_user, target_user, message, clients):
    if target_user in clients:
        clients[target_user].send(f"DM from {sender_user}->  {message}".encode(ENCODER) )
    else:
        clients[sender_user].send("Target User Offline".encode(ENCODER))

##broadcast code logic

def broadcast(host, sender_user, message, hosts, clients):
    if host not in hosts:
        return
    for username in get_users_in_host(host,hosts):
        if username!=sender_user and username in clients:
            clients[username].send(f"[#{host}/{sender_user}] {message}".encode(ENCODER))
