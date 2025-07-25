def add_host(host,hosts):
    if host not in hosts:
        hosts[host] = set()

def remove_host(host,hosts):
    for host in hosts:
        del(hosts[host])

def add_user_to_host(username, host_name, hosts):
    hosts[host_name].add(username)

def remove_user_from_all_hosts(username, hosts):
    for members in hosts.values():
        members.discard(username)

def get_users_in_host(host_name, hosts):
    return hosts.get(host_name, set())

