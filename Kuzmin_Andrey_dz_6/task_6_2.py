our_list = []
max_count = 0

with open('nginx_logs.txt', 'r') as f: # Первая задача
    for line in f.readlines():
        remote_addr, request_type, requested_resource = line.split()[0], line.split()[5], line.split()[6]
        our_list.append((remote_addr, request_type, requested_resource))
    spamer_list = [addr[0] for addr in our_list]

for addr in set(spamer_list): # Вторая задача
    if spamer_list.count(addr) > max_count:
        max_count = spamer_list.count(addr)
        spamer = addr
print(spamer)